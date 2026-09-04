import os
import sys
import traceback

bind = "0.0.0.0:5000"
workers = 4
worker_class = "gthread"
threads = 2

def post_fork(server, worker):
    """
    Inicializa el agente en cada proceso hijo una vez que los archivos 
    del protocolo ya fueron generados de forma física en el Dockerfile.
    """
    try:
        from skywalking import agent, config
        
        collector_address = os.getenv("SW_AGENT_COLLECTOR_BACKEND_SERVICES", "skywalking-oap:12800")
        service_name = os.getenv("SW_AGENT_NAME", "q-immune-mesh-app")
        
        config.init(
            collector_address=collector_address,
            service_name=service_name,
            protocol='http',
            log_reporter_active=True
        )
        agent.start()
        server.log.info(f"🟢 [SKYWALKING TELEMETRÍA OK] Conectado con éxito en el Worker PID {worker.pid}")
    except Exception as e:
        server.log.error(f"❌ [FALLO DE TELEMETRÍA EN WORKER PID {worker.pid}]")
        print(traceback.format_exc(), file=sys.stdout, flush=True)
