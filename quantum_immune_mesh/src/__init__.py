"""
Módulo Matriz de quantum_immune_mesh: Fábrica de Aplicaciones (App Factory Pattern).
Se encarga de inicializar, configurar y acoplar los componentes lógicos de
Inteligencia Artificial, Red, Telemetría y Criptografía Post-Cuántica de la malla.
"""

import os
import gc
import time
from flask import Flask, jsonify, request


def create_app() -> Flask:
    """Fábrica de nivel de producción que inicializa, blinda y puebla la malla."""
    app = Flask(__name__)

    # 1. Configuración rígida del entorno de ejecución corporativo
    app.config["JSON_SORT_KEYS"] = False
    app.config["SECRET_KEY"] = os.environ.get(
        "JWT_SECRET_KEY", "fallback-key-local-segura-2026"
    )

    # 2. Inicialización Avanzada / Warm-up del Motor de IA (Patrón Singleton)
    try:
        from src.ai_engine.detector import DetectorAnomaliasIA

        app.config["AI_DETECTOR"] = DetectorAnomaliasIA()
        app.logger.info("🤖 [AI-ENGINE] Detector de anomalías precargado en RAM con éxito.")
    except Exception as e:
        app.logger.error(f"❌ [AI-ENGINE] Fallo crítico al inicializar el modelo de IA: {str(e)}")

    # 3. Interceptores de Ciclo de Vida Globales (API Management Telemetry Hooks)
    @app.before_request
    def iniciar_contexto_peticion():
        """Inyecta metadatos de gobernanza en la petición antes de tocar los controladores."""
        request.start_time = time.time()
        
        # 🟢 CAPTURA DEL PROCESO DE ENTRADA COMPLETO
        app.logger.info(f"📥 [CAPTURA ENTRADA] {request.method} -> {request.path}")
        app.logger.info(f"📋 HEADERS RECIBIDOS: {dict(request.headers)}")
        if request.is_json:
            app.logger.info(f"📦 BODY JSON ENVIADO: {request.get_json()}")
        else:
            app.logger.info(f"📦 BODY RAW: {request.get_data()}")

    @app.after_request
    def limpiar_recursos_sistema(response):
        """Libera la memoria RAM asignada a las matrices de PennyLane y fuerza la limpieza."""
        # 🟢 CAPTURA DEL PROCESO DE SALIDA COMPLETO (Registra el error 403 o 200)
        app.logger.info(f"📤 [CAPTURA SALIDA] Estatus: {response.status} -> Endpoint: {request.path}")
        
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Quantum-Immune-Status"] = "ACTIVE"

        gc.collect()
        return response

    # 4. Manejadores de Errores Corporativos Centralizados (Clean JSON Global Errors)
    @app.errorhandler(404)
    def recurso_no_encontrado(error):
        return (
            jsonify(
                {
                    "codigo_estatus": 404,
                    "error": "Not Found",
                    "mensaje": "El endpoint o recurso solicitado no existe en la malla mesh.",
                    "solucion": "Verifique el versionamiento explícito en la URL (/api/v1/...).",
                }
            ),
            404,
        )

    @app.errorhandler(401)
    def no_autorizado(error):
        return (
            jsonify(
                {
                    "codigo_estatus": 401,
                    "error": "Unauthorized",
                    "mensaje": "Firma criptográfica post-cuántica inválida, expirada o ausente.",
                    "solucion": "Solicite un token Bearer JWT válido en el endpoint /api/v1/auth/login.",
                }
            ),
            401,
        )

    # 🟢 AGREGADO: CAPTURADOR DE ERROR 403 PARA TRANSPARENCIA DE AUDITORÍA
    @app.errorhandler(403)
    def prohibido(error):
        return (
            jsonify(
                {
                    "codigo_estatus": 403,
                    "error": "Forbidden",
                    "mensaje": "Petición rechazada por políticas corporativas de la malla perimetral.",
                    "solucion": "El cliente no cuenta con los privilegios o el payload falló la validación.",
                }
            ),
            403,
        )

    @app.errorhandler(500)
    def fallo_interno_sistema(error):
        return (
            jsonify(
                {
                    "codigo_estatus": 500,
                    "error": "Internal Server Error",
                    "mensaje": "Colapso matemático o de red interno dentro del clúster de Kubernetes.",
                    "solucion": "Revise los logs de Gunicorn o limpie los pods huérfanos con kubectl delete.",
                }
            ),
            500,
        )

    # 5. Registro de la Capa de API Management y Red (Blueprints)
    from src.routes import mesh_bp
    app.register_blueprint(mesh_bp)

    return app
