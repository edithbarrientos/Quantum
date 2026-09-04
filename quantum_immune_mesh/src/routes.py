"""
Capa de API Management y Red de quantum_immune_mesh.
Controlador perimetral de enrutamiento que intercepta payloads, 
calcula riesgos vía IA y despacha políticas de protección post-cuánticas (PQC).
"""

import os
import time
import uuid
import logging
from flask import Blueprint, request, jsonify, Response
from src.crypto_engine import FabricaCriptograficaPQC
from src.ai_engine import proteger_con_ia

logger = logging.getLogger("QuantumImmuneCrypto")
mesh_bp = Blueprint('mesh', __name__)

VERSION_MALLA = os.environ.get("MESH_VERSION", "v1")
ENTORNO_MALLA = os.environ.get("MESH_ENVIRONMENT", "PROD")


@mesh_bp.route("/api/v1/mesh/auth/keygen", methods=["POST"])
def generar_credenciales_pqc() -> Response:
    correlation_id = str(uuid.uuid4())
    logger.info(f"📥 [APIM] [{correlation_id}] Solicitud de generación de llaves PQC recibida.")
    try:
        # Inferencia limpia y nativa gracias a la estructura Unión de factory.py
        motor_pqc = FabricaCriptograficaPQC.obtener_motor_pqc_configurado()
        credenciales = motor_pqc.generar_par_llaves()
        credenciales["correlation_id"] = correlation_id
        credenciales["environment"] = ENTORNO_MALLA
        credenciales["version"] = VERSION_MALLA
        return jsonify(credenciales), 200
    except Exception as e:
        logger.error(f"❌ [APIM] [{correlation_id}] Fallo crítico en KeyGen: {str(e)}")
        return jsonify({"error": "Fallo interno en la factoría", "correlation_id": correlation_id}), 500


@mesh_bp.route("/api/v1/mesh/quantum/procesar", methods=["POST"])
@proteger_con_ia()  # 🛡️ Cortafuegos cognitivo IA activo: Filtra amenazas antes de la criptografía pesada
def interceptar_y_procesar_trafico() -> Response:
    correlation_id = str(uuid.uuid4())
    tiempo_inicio = time.time()
    datos = request.get_json() or {}
    logger.info(f"📥 [APIM] [{correlation_id}] Interceptando payload perimetral.")

    # Recuperamos de manera segura el análisis de riesgo inyectado por el decorador
    analisis_riesgo = getattr(request, "analisis_riesgo_ia", {"detección_anomalia": False, "status": "NO_EVALUATED"})

    try:
        motor_pqc = FabricaCriptograficaPQC.obtener_motor_pqc_configurado()
        angulo_grados = float(datos.get("angulo_grados", 0.0))
        texto_plano_datos = f"id:{correlation_id}|angulo:{angulo_grados}".encode('utf-8')
        llave_maestra = request.headers.get("X-PQC-Secret-Key", "YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY=")
        
        resultado_criptografico = motor_pqc.procesar_operacion(texto_plano_datos, llave_maestra)
        latencia_ms = round((time.time() - tiempo_inicio) * 1000, 2)

        return jsonify({
            "correlation_id": correlation_id,
            "malla_mesh_status": "SECURE_IMMUNE",
            "evaluacion_ia_perimetral": analisis_riesgo,
            "blindaje_pqc_output": resultado_criptografico,
            "telemetria_rendimiento": {
                "entorno": ENTORNO_MALLA,
                "latencia_procesamiento_ms": latencia_ms
            }
        }), 200
    except Exception as e:
        logger.error(f"❌ [APIM] [{correlation_id}] Colapso: {str(e)}")
        return jsonify({"error": "Internal Error", "correlation_id": correlation_id}), 500