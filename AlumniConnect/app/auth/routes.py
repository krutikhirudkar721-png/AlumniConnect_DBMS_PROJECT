from functools import wraps
from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from werkzeug.security import check_password_hash
from app.database.connection import fetch_one

auth_bp=Blueprint('auth',__name__)
def login_required(view):
    @wraps(view)
    def w(*a,**k): return view(*a,**k) if session.get('user_id') else redirect(url_for('auth.login'))
    return w
def role_required(role):
    def d(view):
        @wraps(view)
        def w(*a,**k): return view(*a,**k) if session.get('role')==role else ('Access denied.',403)
        return w
    return d
@auth_bp.route('/')
def home(): return redirect(url_for('alumni.dashboard') if session.get('user_id') else url_for('auth.login'))
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        u=fetch_one('SELECT * FROM users WHERE email=%s AND is_active=1',(request.form.get('email','').strip(),))
        if u and check_password_hash(u['password_hash'],request.form.get('password','')):
            session.clear(); session.update(user_id=u['user_id'],role=u['role'],alumni_id=u.get('alumni_id')); return redirect(url_for('alumni.dashboard'))
        flash('Invalid email or password.','error')
    return render_template('login.html')
@auth_bp.route('/logout')
def logout(): session.clear(); return redirect(url_for('auth.login'))
