from flask import Flask
from src.routes import quantum_bp

def create_app():
    """Fábrica de aplicaciones encargada de levantar configuraciones y rutas."""
    app = Flask(__name__)
    
    # Registramos de forma limpia las rutas del Blueprint cuántico
    app.register_blueprint(quantum_bp)
    
    return app
