# 🛡️ Quantum Immune Mesh - Gobernanza Adaptativa e Inmunidad Post-Cuántica (PQC)

## 🎯 Objetivo de la Prueba de Concepto (PoC)
Esta arquitectura avanzada diseña, blinda y gobierna un perímetro de servicios crítico (API Management) capaz de resistir ataques criptoanalíticos cuánticos futuros (**Día Q**) mediante el uso de **Inteligencia Artificial adaptativa** y algoritmos estandarizados por el **NIST**.

El sistema actúa como una malla de confianza cero (**Zero-Trust Mesh**) que intercepta payloads corporativos clásicos, evalúa patrones de amenaza perimetral en milisegundos mediante un clasificador cognitivo de Machine Learning y conmuta dinámicamente sus directivas de protección utilizando el esquema de encapsulación post-cuántica **ML-KEM (Kyber768)**, garantizando la soberanía de los datos de forma agnóstica.

---

# 🛡️ Quantum Immune Mesh - Gobernanza Adaptativa e Inmunidad Post-Cuántica (PQC)

## 🎯 Objetivo de la Prueba de Concepto (PoC)
Esta arquitectura avanzada diseña, blinda y gobierna un perímetro de servicios crítico (API Management) capaz de resistir ataques criptoanalíticos cuánticos futuros (**Día Q**) mediante el uso de **Inteligencia Artificial adaptativa** y algoritmos estandarizados por el **NIST**.

El sistema actúa como una malla de confianza cero (**Zero-Trust Mesh**) que intercepta payloads corporativos clásicos, evalúa patrones de amenaza perimetral en milisegundos mediante un clasificador cognitivo de Machine Learning y conmuta dinámicamente sus directivas de protección utilizando el esquema de encapsulación post-cuántica **ML-KEM (Kyber768)**, garantizando la soberanía de los datos de forma agnóstica.

---

## 🗺️ 1. Diagrama de Arquitectura Global de Infraestructura y Software

# 🛡️ Quantum Immune Mesh - Gobernanza Adaptativa e Inmunidad Post-Cuántica (PQC)

## 🎯 Objetivo de la Prueba de Concepto (PoC)
Esta arquitectura avanzada diseña, blinda y gobierna un perímetro de servicios crítico (API Management) capaz de resistir ataques criptoanalíticos cuánticos futuros (**Día Q**) mediante el uso de **Inteligencia Artificial adaptativa** y algoritmos estandarizados por el **NIST**.

El sistema actúa como una malla de confianza cero (**Zero-Trust Mesh**) que intercepta payloads corporativos clásicos, evalúa patrones de amenaza perimetral en milisegundos mediante un clasificador cognitivo de Machine Learning y conmuta dinámicamente sus directivas de protección utilizando el esquema de encapsulación post-cuántica **ML-KEM (Kyber768)**, garantizando la soberanía de los datos de forma agnóstica.

---

## 🗺️ 1. Diagrama de Arquitectura Global de Componentes e Infraestructura Multinivel

```text
==================================================================================================
 NIVEL 0 & NIVEL 1: ENTRADA DE TRÁFICO, HARDWARE HOST Y CAPA DE VIRTUALIZACIÓN
==================================================================================================

 [ Client / curl Request ] ───( Solicitud HTTP POST )───► [ Puerto Seguro Host: 8080 ]
                                                                     │
                                                                     ▼ ( Canal Port-Forward )
 ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 │ [ Host System Layer - lo0 Interface ] ➔ IP Privada Dedicada Perimetral: 172.20.0.50          │
 ├──────────────────────────────────────────────────────────────────────────────────────────────┤
 │ [ Hypervisor / VM Colima Linux Kernel ] ➔ Aislamiento nativo de cómputo, CPU Sockets y RAM   │
 └───────────────────────────────────────────────────────────┬──────────────────────────────────┘
                                                             ▼ Sincronización Interna del Clúster
==================================================================================================
 NIVEL 2 EN ADELANTE: ORQUESTACIÓN EN KUBERNETES Y ENCAPSULACIÓN DE COMPONENTES POR PODS
==================================================================================================

 ☸️ LOCAL KUBERNETES CONTROL PLANE (Namespace: default)
 │
 ├── [ Nivel 2: Ingress Controller Object ] ───► Aplica Directiva de Clase de Red: apisix
 │                                                                   │
 │                                                                   ▼ Balancea Tráfico Capa 7
 │  ╔══════════════════════════════════════════════════════════════════════════════════════════╗
 ├──║ [ Nivel 2 ] Pod: apisix-7fd8c6b84f-ctxnw (API Gateway Edge Pod)                          ║
 │  ║   └── 🐳 CONTAINER: apisix-gateway-engine                                                ║
 │  ║        └── ⚙️ [ Componente: Proxy Reverso Perimetral ] ◄─────────────────────────────────╢
 │  ╚══════════════════════════════════════════════════════════════════════════════════════════╝
 │                                                                   │ Interroga e Inyecta Rutas
 │  ╔════════════════════════════════════════════════════════════════▼═════════════════════════╗
 ├──║ [ Nivel 2 ] Pod: apisix-etcd-0 (StatefulSet Distributed Data Store Pod)                  ║
 │  ║   └── 🐳 CONTAINER: etcd-memory-datastore                                                ║
 │  ║        └── ⚙️ [ Componente: Raft Datastore Key/Value en RAM ] ◄──────────────────────────╢
 │  ╚══════════════════════════════════════════════════════════════════════════════════════════╝
 │
 │  ╔══════════════════════════════════════════════════════════════════════════════════════════╗
 └──║ Pod: q-immune-mesh-deployment-5c9b89445c-5tg6f (Core Microservice - 1 Réplica)           ║
    ║   └── 🐳 CONTAINER: mesh-app-container (Python 3.11-slim Engine)                         ║
    ║        │                                                                                 ║
    ║        ├── [ Nivel 3: Capa de Aplicación ] ➔ ⚙️ [ Componente: Servidor Gunicorn WSGI ]   ║
    ║        │    └── Workers síncronos en RAM ───► Inicializa en frío e infla runtime         ║
    ║        │                                           │                                     ║
    ║        ▼                                           ▼ Contextualiza Endpoints de Red      ║
    ║    ┌──────────────────────────────────────────────────────────────────────────────────┐  ║
    ║    │ [ Nivel 3 ] ⚙️ COMPONENTE: Flask App Factory Framework (src/__init__.py)         │  ║
    ║    │    • Hooks de Ciclo de Vida Globales (before_request / after_request Telemetría) │  ║
    ║    │    • Manejador Centralizado de Excepciones de Seguridad (JSON Handlers)          │  ║
    ║    └──────────────────────────────┬───────────────────────────────────────────────────┘  ║
    ║                                   │ Despacha el payload entrante y extrae cabeceras HTTP ║
    ║                                   ▼                                                      ║
    ║    ┌──────────────────────────────────────────────────────────────────────────────── Platica
    ║    │ [ Nivel 4: Capa de IA ] 🧠 COMPONENTE: DetectorAnomaliasIA (detector.py)         │  ║
    ║    │    ➔ PATRÓN DE DISEÑO GOF: SINGLETON                                             │  ║
    ║    │    • Extrae métricas en caliente: Payload size, Burst rate y Token entropy.      │  ║
    ║    │    • Evalúa la Sigmoide con parámetros del K8s Secret: z = w·x + b               │  ║
    ║    │    • Emite directivas adaptativas (Probabilidad > 0.75 ➔ UPGRADE_PQC_REQUIREMENT)│  ║
    ║    └──────────────────────────────┬───────────────────────────────────────────────────┘  ║
    ║                                   │ Si el tráfico es pacífico/aprobado, delega el cifrado║
    ║                                   ▼                                                      ║
    ║    ┌──────────────────────────────────────────────────────────────────────────────────┐  ║
    ║    │ [ Nivel 5: Capa Criptográfica ] 🏭 COMPONENTE: FabricaCriptograficaPQC           │  ║
    ║    │    ➔ PATRÓN DE DISEÑO GOF: ABSTRACT FACTORY                                      │  ║
    ║    │    • Conmuta dinámicamente la familia del algoritmo según variables de entorno.  │  ║
    ║    │                                                                                  │  ║
    ║    │    ├── 🔒 Sub-Componente Strategy [ ML-DSA / Dilithium3 ] ➔ Firma digital         │  ║
    ║    │    └── 🔒 Sub-Componente Strategy [ ML-KEM / Kyber768 ]   ➔ Encapsulación NIST    │  ║
    ║    │             │                                                                    │  ║
    ║    │             ▼ Inicializa sub-proceso matemático en la RAM de Linux               │  ║
    ║    │         ┌───────────────────────────────────────────────────────────────────┐    │  ║
    ║    │         │ 🔒 Sub-Engine: AES-GCM Encryptor (src/crypto_engine/strategies.py)│     │  ║
    ║    │         │    • Auto-genera un Vector de Inicialización (Nonce) de 12B en RAM│    │  ║
    ║    │         │    • Output: Retorna el Criptograma binario limpio.               │    │  ║
    ║    │         └───────────────────────────────────────────────────────────────────┘    │  ║
    ║    └──────────────────────────────────────────────────────────────────────────────────┘  ║
    ╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

### ⏱️ 1.2 Diagrama de Secuencia de Arquitectura Cognitiva (APIM Request Lifecycle)

El siguiente ciclo de vida describe cómo se intercepta una petición a través de las fronteras físicas de la infraestructura de contenedores, cómo actúa la frontera logística de Machine Learning y cómo el patrón Abstract Factory encapsula los Secrets de Kubernetes de forma stateless:

```text
[ Cliente / curl ]      [ Apache APISIX ]       [ API: routes.py ]     [ Singleton: IA ]     [ Factory: PQC ]
        │                       │                       │                       │                     │
        │───( POST /procesar )─►│                       │                       │                     │
        │    X-Burst-Rate: 1    │───( Forwarding )─────►│                       │                     │
        │                       │                       │───( Extrae Cabeceras )►│                    │
        │                       │                       │                       │                     │
        │                       │                       │                       │───( Evalúa Sigmoide)│
        │                       │                       │                       │     z = w·x + b     │
        │                       │                       │◄──( Retorna Riesgo )──│                     │
        │                       │                       │    Anomalía: False    │                     │
        │                       │                       │    Mitigación: Ok     │                     │
        │                       │                       │                       │                     │
        │                       │                       │───( Solicita Motor )───────────────────────►│
        │                       │                       │    PQC_ACTIVE_ENGINE  │                     │
        │                       │                       │                       │                     │
        │                       │                       │                       │◄──( Instancia KEM )─│
        │                       │                       │                       │     Kyber768        │
        │                       │                       │                       │                     │
        │                       │                       │───( Ejecuta Cifrado )──────────────────────►│
        │                       │                       │    Gira un Nonce 12B  │                     │
        │                       │                       │                       │                     │
        │                       │                       │◄──( Criptograma GCM )───────────────────────│
        │                       │                       │                                             │
        │◄──( HTTP 200 OK )─────│◄──( Return JSON )─────│                                             │
        │    Payload Blindado   │                                                                     │
```

---

## 📥 3. Especificación de Contratos e Intercambio de Datos

### **A. Intercepción de Tráfico y Cifrado PQC Adaptativo**
### **POST** `/api/v1/mesh/quantum/procesar`
Analiza la ráfaga de tráfico y encripta el payload corporativo con criptografía inmune al ordenador cuántico.

*   **Cabeceras de Entrada de Auditoría:**
    *   `X-Burst-Rate: 1` (Velocidad de ráfaga simulada)
    *   `Authorization: Bearer eyJhbGciOiJI...` (Métrica de entropía por longitud)
*   **Cuerpo del JSON de Entrada (Request Payload):**
```json
{
  "client_id": "corp-dev-01",
  "action": "execute_quantum_safe_payload"
}
```
*   **Cuerpo del JSON de Salida (Response Payload - 200 OK):**
```json
{
  "correlation_id": "a3514e3a-964e-4b1c-899c-931a065325d2",
  "malla_mesh_status": "SECURE_IMMUNE",
  "evaluacion_ia_perimetral": {
    "modelo_auditor": "AegisCoreClassifier",
    "probabilidad_amenaza": 0.7658,
    "detección_anomalia": true,
    "estrategia_mitigacion_sugerida": "UPGRADE_PQC_REQUIREMENT",
    "umbral_configurado": 0.75
  },
  "blindaje_pqc_output": {
    "mecanismo": "Kyber768-KEM-AES-GCM",
    "nonce_b64": "rNlmP7UF7+lRwW61",
    "payload_criptograma_b64": "GF6KSSIwsux4M65ltpT2wRjkGPdafROXgYFnb69a5vXa+..."
  },
  "telemetria_rendimiento": {
    "entorno": "PROD",
    "latencia_procesamiento_ms": 20.51
  }
}
```

---

## 📁 4. Jerarquía Estructurada del Repositorio
El árbol de ficheros sigue estrictamente los principios de alta cohesión y bajo acoplamiento:

```text
📂 quantum_immune_mesh/
│
├── 📝 requirements.txt      # Dependencias congeladas (Flask, Scikit-Learn, PyJWT, Cryptography)
├── 🐳 Dockerfile            # Configuración de capas y búferes del contenedor para Gunicorn WSGI
├── 🚀 run.py                # Punto de entrada WSGI oficial (Expone la variable global :app)
├── 📖 README.md             # Especificación arquitectónica del portafolio (Este archivo)
│
├── 📂 src/                  # 🛠️ CÓDIGO FUENTE CON IMPLEMENTACIÓN DE PATRONES DE DISEÑO GOF
│   ├── ⚙️ __init__.py        # App Factory: Precarga analítica en frío y contexto global de Flask
│   ├── 📡 routes.py          # API Management: Enrutador perimetral, logs y correlation IDs
│   │
│   ├── 📂 ai_engine/        # 🧠 CAPA COGNITIVA DE MACHINE LEARNING
│   │   └── 🔬 detector.py    # Patrón GoF Singleton: Clasificador logístico sigmoide perimetral
│   │
│   └── 📂 crypto_engine/    # 🔒 NÚCLEO CRIPTOGRÁFICO POST-CUÁNTICA (PQC DEL NIST)
│       ├── 🏭 factory.py     # Patrón GoF Abstract Factory: Conmutador declarativo de familias cripto
│       └── 🛡️ strategies.py  # Patrón GoF Strategy: Operaciones modulares Kyber/Dilithium + Nonce RAM
│
└── 📂 k8s_infra/            # ☸️ ORQUESTACIÓN DECLARATIVA PARAMETRIZADA (ENTORNO OFFLINE)
    ├── 🧱 01-infraestructura.yaml # Orquestación del Kubernetes Deployment (1 Réplica) y ClusterIP
    └── 🔑 02-secrets.yaml        # Bóveda Opaque cifrada en Base64 para hiperparámetros de la sigmoide
```


---

## 🚀 5. Secuencia de Despliegue Local (Entorno 100% Offline)

Para levantar e inmunizar tu infraestructura de forma limpia, ejecuta esta secuencia ordenada:

```bash
# 1. Vincular la terminal con el motor de Docker de Colima en tu Mac
export DOCKER_HOST="unix://\$HOME/.colima/default/docker.sock"

# 2. Compilar la imagen del microservicio inteligente de forma limpia
docker build -t q-immune-mesh-img:latest .

# 3. Lanzar la orquestación declarativa de secretos e infraestructura
kubectl apply -f k8s_infra/02-secrets.yaml
kubectl apply -f k8s_infra/01-infraestructura.yaml

# 4. Forzar la recreación destructiva para limpiar cachés viejas
kubectl delete pods -l app=q-immune-mesh --force --grace-period=0

# 5. Abrir el puente de red virtual seguro en tu puerto preferido
kubectl port-forward --address 0.0.0.0 service/q-immune-mesh-service 8080:5000
```

---

## 🚀 6. Guía de Operaciones e Inyección Manual

Debido a que el Gateway opera bajo configuraciones dinámicas directas en su almacén `etcd`, sigue rigurosamente este orden secuencial para inicializar y validar las comunicaciones del entorno local:

### 🔐 1. Inyección de Reglas en el API Gateway (Admin API)
Para romper la barrera perimetral y registrar las rutas de negocio, expón el canal de administración e inyecta la configuración en el clúster:

```bash
# Paso A: Levantar túnel de administración de APISIX (Pestaña Terminal 1)
kubectl port-forward --address 0.0.0.0 service/apisix-admin 9180:9180

# Paso B: Inyectar la ruta utilizando el Token Maestro de APISIX v3 (Pestaña Terminal 2)
curl -i -X PUT http://localhost:9180/apisix/admin/routes/q-mesh-route \
     -H "X-API-KEY: edd1c9f034335f136f87ad84b625c8f1" \
     -H "Content-Type: application/json" \
     -d '{
       "uri": "/api/v1/mesh/*",
       "upstream": {
         "type": "roundrobin",
         "nodes": {
           "q-immune-mesh-service.default.svc.cluster.local:5000": 1
         }
       }
     }'
```

### 📡 2. Exposición del Gateway y Pruebas de API Cuántica
Una vez registrada la ruta con código exitoso `200 OK`, procede a enviar tráfico real de prueba hacia tu microservicio en Python:

```bash
# Paso A: Levantar túnel del Gateway de Datos (Pestaña Terminal 3)
kubectl port-forward --address 0.0.0.0 service/apisix-gateway 9080:80

# Paso B: Ejecutar Petición de Procesamiento de Payload PQC Cifrado (Pestaña Terminal 4)
curl -i -X POST http://localhost:9080/api/v1/mesh/quantum/procesar \
     -H "Content-Type: application/json" \
     -H "X-Burst-Rate: 1" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
     -d '\''{"client_id": "corp-dev-01", "action": "execute_quantum_safe_payload"}'\''
```

### 📊 7. Acceso a la Telemetría de SkyWalking
Monitorea la latencia en microsegundos y la topología viva de la red de manera gráfica. Evita colisiones con el puerto ocupado `8080` de tu máquina local redirigiendo el canal visual:

```bash
# Paso A: Levantar túnel de visualización alternativo (Pestaña Terminal 5)
kubectl port-forward --address 0.0.0.0 service/skywalking-ui 8888:8080
```
👉 Accede de manera inmediata desde tu navegador web a la dirección: **[http://localhost:8888](http://localhost:8888)**

---

## 🛡️ Estructura de Parámetros y Secretos Activos (`02-secrets.yaml`)
El microservicio consume las siguientes llaves del objeto `q-immune-mesh-secrets` descodificadas automáticamente en runtime:
* `pqc-active-engine`: Motor `KYBER` activo del NIST.
* `pqc-kyber-variant`: Variante de nivel de seguridad 3 (`Kyber768`).
* `ai-bias`: Coeficiente de frontera calibrado a un sesgo estricto de `-2
---

## 👁️ 8. Evolución Complementaria: Fase 3 - Observabilidad de Grado Corporativo con Apache SkyWalking

Para garantizar la gobernanza total, el rastreo distribuido y el perfilamiento de rendimiento de los motores analíticos/criptográficos en producción, el roadmap contempla la integración de **Apache SkyWalking** como la plataforma centralizada de **APM (Application Performance Monitoring)**:

### 🧩 Arquitectura de Monitoreo No Invasivo (Stateless Mesh Tracing)
```text
 ┌───────────────────────┐      ┌─────────────────────────┐      ┌────────────────────────┐
 │ Pod: apisix-gateway   │      │ Pod: q-immune-mesh      │      │ Pod: skywalking-oap    │
 │ (Tracing Plugin Svc)  │      │ (SkyWalking Python Agent)│     │ (Observability Engine) │
 └───────────┬───────────┘      └────────────┬────────────┘      └───────────┬────────────┘
             │                               │                               │
             │───( Trace Protocol Layer )───►│                               │
             │    Inyecta Sw8 Carrier Header │───( Reporte de Métricas )────►│
             │                               │    Mide Latencia de Kyber/IA  │───► [ UI Dashboard ]
```

### **Métricas Críticas de Negocio a Monitorear (OAP Analytics):**
1.  **Latencia de Conmutación PQC**: Monitoreo dedicado del tiempo de ejecución del patrón *Strategy* al pasar de firmas clásicas a **Kyber768**, aislando el costo computacional del cifrado simétrico AES-GCM en la RAM.
2.  **Saturación del Firewall Cognitivo**: Registro del throughput de peticiones desviadas hacia el *Singleton* de Inteligencia Artificial, graficando en tiempo real la tasa de bloqueos `403 Forbidden` frente a accesos legítimos `200 OK`.
3.  **Topología Dinámica del Clúster**: Generación automática del mapa de dependencias vivas del clúster de Kubernetes, midiendo las latencias de tránsito desde el Ingress de Apache APISIX hacia los endpoints internos del microservicio.
