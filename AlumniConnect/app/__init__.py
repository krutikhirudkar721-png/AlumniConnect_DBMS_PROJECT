from flask import Flask
from config import Config

def create_app():
    app=Flask(__name__); app.config.from_object(Config)
    from app.auth.routes import auth_bp
    from app.alumni.routes import alumni_bp
    from app.reports.routes import reports_bp
    app.register_blueprint(auth_bp); app.register_blueprint(alumni_bp); app.register_blueprint(reports_bp)
    @app.errorhandler(403)
    def forbidden(e): return 'Access denied.',403
    @app.errorhandler(404)
    def missing(e): return 'Page not found.',404
    @app.errorhandler(500)
    def server(e): return 'An unexpected server error occurred.',500
    return app
