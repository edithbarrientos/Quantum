"""
Módulo de Decoradores Perimetrales de quantum_immune_mesh.
Filtra y audita payloads mediante telemetría cognitiva con Scikit-Learn
antes de permitir la ejecución de operaciones criptográficas post-cuánticas pesadas.
"""

from functools import wraps
from flask import request, jsonify, current_app


def proteger_con_ia():
    """
    Decorador de producción para interceptar peticiones HTTP, evaluar riesgos
    vía el detector de anomalías (IA) y bloquear/mitigar ataques en tiempo real.
    """
    def decorador(f):
        @wraps(f)
        def funcion_decorada(*args, **kwargs):
            datos = request.get_json() or {}

            # 1. Extracción homogeneizada de telemetría perimetral para el modelo de IA
            tamano_payload = len(str(datos))
            velocidad_burst = int(request.headers.get("X-Burst-Rate", "1"))
            token_bearer = request.headers.get("Authorization", "")
            entropia_token = float(len(token_bearer)) / 100.0 if token_bearer else 0.0

            # 2. Recuperación del Singleton del motor de IA precargado en RAM
            detector_ia = current_app.config.get("AI_DETECTOR")
            
            if not detector_ia:
                current_app.logger.error("❌ [AI-DECORATOR] El Singleton AI_DETECTOR no se encuentra inicializado en app.config.")
                # Modo Fail-Safe corporativo: si el motor de IA no cargó, permitimos el flujo pero alertamos
                request.analisis_riesgo_ia = {"detección_anomalia": False, "status": "AI_NOT_INITIALIZED"}  # type: ignore
                return f(*args, **kwargs)

            try:
                # 3. Invocación de la inferencia matemática optimizada
                analisis_riesgo = detector_ia.evaluar_trafico_perimetral(
                    tamano_payload, velocidad_burst, entropia_token
                )

                # 4. Cortafuegos cognitivo: Bloqueo inmediato ante amenazas críticas detectadas por IA
                if analisis_riesgo.get("detección_anomalia") and analisis_riesgo.get("estrategia_mitigacion_sugerida") == "CRITICAL_LOCKOUT":
                    current_app.logger.warning("🚨 [AI-FIREWALL] Petición abortada perimetralmente. Anomalía crítica confirmada.")
                    return jsonify({
                        "error": "Rechazado por firewall cognitivo IA",
                        "correlation_id": getattr(request, "correlation_id", "N/A"),
                        "evaluacion_ia": analisis_riesgo
                    }), 403

                # 5. Inyección del resultado analítico en el contexto para consumo de la ruta
                request.analisis_riesgo_ia = analisis_riesgo  # type: ignore

            except Exception as e:
                # Tolerancia a fallos: si la IA falla por saturación de CPU, la API no se cae
                current_app.logger.error(f"⚠️ [AI-DECORATOR-BYPASS] Fallo en inferencia analítica: {str(e)}")
                request.analisis_riesgo_ia = {"detección_anomalia": False, "status": "BYPASS_MODE_ACTIVE"}  # type: ignore

            return f(*args, **kwargs)
        return funcion_decorada
    return decorador