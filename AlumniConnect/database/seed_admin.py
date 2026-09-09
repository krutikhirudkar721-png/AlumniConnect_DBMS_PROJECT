from werkzeug.security import generate_password_hash
print('ADMIN:',generate_password_hash('Admin@123'))
print('ALUMNI:',generate_password_hash('Alumni@123'))
