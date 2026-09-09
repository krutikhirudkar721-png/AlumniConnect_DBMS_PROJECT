from flask import Blueprint,render_template
from app.auth.routes import login_required,role_required
from app.database.connection import fetch_all
reports_bp=Blueprint('reports',__name__,url_prefix='/reports')
@reports_bp.route('/')
@login_required
@role_required('ADMIN')
def reports():
    dept=fetch_all('SELECT d.department_name,COUNT(a.alumni_id) total FROM departments d LEFT JOIN alumni a ON d.department_id=a.department_id GROUP BY d.department_id ORDER BY total DESC')
    industry=fetch_all('SELECT co.industry,COUNT(DISTINCT ch.alumni_id) total FROM career_history ch JOIN companies co ON ch.company_id=co.company_id WHERE ch.is_current=1 GROUP BY co.industry ORDER BY total DESC')
    skills=fetch_all('SELECT s.skill_name,COUNT(*) total FROM alumni_skills x JOIN skills s ON x.skill_id=s.skill_id GROUP BY s.skill_id ORDER BY total DESC LIMIT 10')
    companies=fetch_all('SELECT co.company_name,COUNT(DISTINCT ch.alumni_id) total FROM career_history ch JOIN companies co ON ch.company_id=co.company_id WHERE ch.is_current=1 GROUP BY co.company_id ORDER BY total DESC LIMIT 10')
    mentors=fetch_all('SELECT a.alumni_id,CONCAT(a.first_name," ",a.last_name) full_name,a.email,m.domain,m.topics FROM mentorship m JOIN alumni a ON m.alumni_id=a.alumni_id WHERE m.is_available=1')
    return render_template('reports.html',dept=dept,industry=industry,skills=skills,companies=companies,mentors=mentors)
