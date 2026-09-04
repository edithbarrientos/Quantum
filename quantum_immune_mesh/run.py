import sys
import logging
import traceback

# 1. CONFIGURACIÓN DE LOGS COMPATIBLE
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] [%(levelname)s] - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger('quantum_mesh_logger')
logger.info("Inicializando cargador del nodo perimetral Quantum Immune Mesh...")

# ==============================================================================
# 2. CAPTURA OPERATIVA AVANZADA DE ERRORES DE ARRANQUE (FLASK NATIVO)
# ==============================================================================
try:
    from src import create_app
    app = create_app()
    logger.info("🚀 Aplicación Flask instanciada con éxito y lista para producción.")
    
except Exception as e:
    logger.error("❌ [FALLO CRÍTICO AL INICIALIZAR LA APP EN EL WORKER]")
    error_detallado = traceback.format_exc()
    print(error_detallado, file=sys.stdout, flush=True)
    sys.exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
