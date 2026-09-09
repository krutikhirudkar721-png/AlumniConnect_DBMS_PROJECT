from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from app.auth.routes import login_required,role_required
from app.database.connection import fetch_all,fetch_one,execute,get_db

alumni_bp=Blueprint('alumni',__name__,url_prefix='/alumni')
@alumni_bp.route('/dashboard')
@login_required
def dashboard():
    stats={k:fetch_one(q)['n'] for k,q in {'alumni':'SELECT COUNT(*) n FROM alumni','departments':'SELECT COUNT(*) n FROM departments','companies':'SELECT COUNT(*) n FROM companies','skills':'SELECT COUNT(*) n FROM skills','mentors':'SELECT COUNT(*) n FROM mentorship WHERE is_available=1'}.items()}
    dept=fetch_all('SELECT d.department_name,COUNT(a.alumni_id) total FROM departments d LEFT JOIN alumni a ON d.department_id=a.department_id GROUP BY d.department_id ORDER BY total DESC')
    batch=fetch_all('SELECT graduation_year,COUNT(*) total FROM alumni GROUP BY graduation_year ORDER BY graduation_year DESC')
    return render_template('dashboard.html',stats=stats,dept=dept,batch=batch)
@alumni_bp.route('/')
@login_required
def directory():
    f={k:request.args.get(k,'').strip() for k in ['name','department','graduation_year','company','designation','industry','location','skill','mentor','min_experience']}; c=[]; p=[]
    if f['name']: c.append('(a.first_name LIKE %s OR a.last_name LIKE %s)'); p += [f"%{f['name']}%",f"%{f['name']}%"]
    for key,sql in [('department','d.department_name=%s'),('graduation_year','a.graduation_year=%s'),('company','co.company_name=%s'),('industry','co.industry=%s')]:
        if f[key]: c.append(sql); p.append(f[key])
    if f['designation']: c.append('ch.designation LIKE %s'); p.append('%'+f['designation']+'%')
    if f['location']: c.append('a.location LIKE %s'); p.append('%'+f['location']+'%')
    if f['skill']: c.append('EXISTS (SELECT 1 FROM alumni_skills z JOIN skills zz ON z.skill_id=zz.skill_id WHERE z.alumni_id=a.alumni_id AND zz.skill_name=%s)'); p.append(f['skill'])
    if f['mentor']=='yes': c.append('EXISTS (SELECT 1 FROM mentorship m WHERE m.alumni_id=a.alumni_id AND m.is_available=1)')
    if f['mentor']=='no': c.append('NOT EXISTS (SELECT 1 FROM mentorship m WHERE m.alumni_id=a.alumni_id AND m.is_available=1)')
    if f['min_experience'].isdigit(): c.append('(SELECT COALESCE(SUM(TIMESTAMPDIFF(MONTH,x.start_date,COALESCE(x.end_date,CURDATE()))),0) FROM career_history x WHERE x.alumni_id=a.alumni_id) >= %s*12'); p.append(int(f['min_experience']))
    where=(' WHERE '+' AND '.join(c)) if c else ''
    q=f'''SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) full_name,a.email,a.location,a.graduation_year,d.department_name,co.company_name,ch.designation,co.industry,COALESCE(GROUP_CONCAT(DISTINCT s.skill_name SEPARATOR ', '),'') skills FROM alumni a LEFT JOIN departments d ON a.department_id=d.department_id LEFT JOIN career_history ch ON a.alumni_id=ch.alumni_id AND ch.is_current=1 LEFT JOIN companies co ON ch.company_id=co.company_id LEFT JOIN alumni_skills aks ON a.alumni_id=aks.alumni_id LEFT JOIN skills s ON aks.skill_id=s.skill_id {where} GROUP BY a.alumni_id,full_name,a.email,a.location,a.graduation_year,d.department_name,co.company_name,ch.designation,co.industry ORDER BY a.last_name,a.first_name'''
    rows=fetch_all(q,tuple(p)); return render_template('alumni.html',alumni=rows,filters=f,departments=fetch_all('SELECT * FROM departments ORDER BY department_name'),companies=fetch_all('SELECT * FROM companies ORDER BY company_name'),skills=fetch_all('SELECT * FROM skills ORDER BY skill_name'),industries=fetch_all('SELECT DISTINCT industry FROM companies WHERE industry IS NOT NULL ORDER BY industry'))
@alumni_bp.route('/<int:aid>')
@login_required
def profile(aid):
    person=fetch_one('SELECT a.*,d.department_name FROM alumni a LEFT JOIN departments d ON a.department_id=d.department_id WHERE a.alumni_id=%s',(aid,))
    if not person:return 'Alumni not found.',404
    edu=fetch_all('SELECT * FROM education WHERE alumni_id=%s ORDER BY graduation_year DESC',(aid,)); career=fetch_all('SELECT ch.*,co.company_name,co.industry FROM career_history ch JOIN companies co ON ch.company_id=co.company_id WHERE ch.alumni_id=%s ORDER BY ch.start_date DESC',(aid,)); skills=fetch_all('SELECT s.skill_name,aks.skill_level FROM alumni_skills aks JOIN skills s ON aks.skill_id=s.skill_id WHERE aks.alumni_id=%s',(aid,)); mentor=fetch_one('SELECT * FROM mentorship WHERE alumni_id=%s',(aid,))
    return render_template('alumni_profile.html',person=person,edu=edu,career=career,skills=skills,mentor=mentor)
@alumni_bp.route('/add',methods=['GET','POST'])
@login_required
@role_required('ADMIN')
def add():
    deps=fetch_all('SELECT * FROM departments ORDER BY department_name')
    if request.method=='POST':
        f=request.form
        try:
            c=get_db(); cur=c.cursor(); cur.execute('INSERT INTO alumni(first_name,last_name,email,phone,location,department_id,graduation_year) VALUES(%s,%s,%s,%s,%s,%s,%s)',tuple(f.get(x) for x in ['first_name','last_name','email','phone','location','department_id','graduation_year'])); aid=cur.lastrowid
            if f.get('career_company') and f.get('career_designation'):
                cur.execute('SELECT company_id FROM companies WHERE company_name=%s',(f['career_company'],)); r=cur.fetchone()
                if r: cid=r[0]
                else: cur.execute('INSERT INTO companies(company_name,industry,location) VALUES(%s,%s,%s)',(f['career_company'],f.get('career_industry'),f.get('career_location'))) or (cid:=cur.lastrowid)
                cur.execute('INSERT INTO career_history(alumni_id,company_id,designation,job_location,start_date,is_current) VALUES(%s,%s,%s,%s,COALESCE(%s,CURDATE()),1)',(aid,cid,f['career_designation'],f.get('career_location'),f.get('career_start') or None))
            c.commit(); cur.close(); c.close(); flash('Alumni added successfully.','success'); return redirect(url_for('alumni.profile',aid=aid))
        except Exception: flash('Could not save the alumni record. Check duplicate email and values.','error')
    return render_template('add_alumni.html',departments=deps)
@alumni_bp.route('/<int:aid>/edit',methods=['GET','POST'])
@login_required
def edit(aid):
    if session.get('role')!='ADMIN' and session.get('alumni_id')!=aid:return 'Access denied.',403
    person=fetch_one('SELECT * FROM alumni WHERE alumni_id=%s',(aid,)); deps=fetch_all('SELECT * FROM departments ORDER BY department_name')
    if request.method=='POST':
        f=request.form
        try: execute('UPDATE alumni SET first_name=%s,last_name=%s,email=%s,phone=%s,location=%s,department_id=%s,graduation_year=%s WHERE alumni_id=%s',(f['first_name'],f['last_name'],f['email'],f.get('phone'),f.get('location'),f['department_id'],f['graduation_year'],aid)); flash('Profile updated.','success'); return redirect(url_for('alumni.profile',aid=aid))
        except Exception: flash('Unable to update profile.','error')
    return render_template('edit_alumni.html',person=person,departments=deps)
@alumni_bp.route('/<int:aid>/delete',methods=['POST'])
@login_required
@role_required('ADMIN')
def delete(aid):
    try: execute('DELETE FROM alumni WHERE alumni_id=%s',(aid,)); flash('Alumni deleted.','success')
    except Exception: flash('Could not delete this alumni record.','error')
    return redirect(url_for('alumni.directory'))
