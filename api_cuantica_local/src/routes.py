from flask import Blueprint, request, jsonify
from src.quantum_engine import ejecutar_circuito_cuantico, np

# Instanciamos el Blueprint para modularizar las rutas cuánticas de la app
quantum_bp = Blueprint('quantum', __name__)

@quantum_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online", 
        "architecture": "Modular Factory Pattern",
        "environment": "Docker Container (Linux)",
        "backend": "Gunicorn Puro (WSGI)", 
        "quantum_simulator": "Local (default.qubit)"
    })

@quantum_bp.route("/api/v1/quantum/procesar", methods=["POST"])
def procesar_matrices_cuanticas():
    datos = request.get_json() or {}
    
    id_solicitud = datos.get("id_solicitud", "SINFIRM")
    angulo_grados = float(datos.get("angulo_grados", 0.0))
    
    # Conversión matemática clásica a radianes para alimentar las compuertas
    radianes = (angulo_grados * np.pi) / 180.0
    
    # Invocamos al procesador cuántico local pasándole el parámetro clásico
    resultado_probabilidades = ejecutar_circuito_cuantico(radianes)
    
    estados = ["00", "01", "10", "11"]
    distribucion = {estados[i]: f"{float(resultado_probabilidades[i])*100:.2f}%" for i in range(4)}
    
    return jsonify({
        "id_solicitud": id_solicitud,
        "angulo_procesado_rad": round(radianes, 4),
        "distribucion_de_probabilidad": distribucion,
        "estado_mas_probable": estados[np.argmax(resultado_probabilidades)]
    })
