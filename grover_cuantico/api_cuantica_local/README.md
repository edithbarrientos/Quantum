# ⚛️ API Cuántica Local Contenerizada - Arquitectura Segura en Kubernetes con JWT

## 🎯 Objetivo de la Prueba de Concepto (PoC)
El objetivo de esta Prueba de Concepto es **validar la integración, gobernanza y blindaje criptográfico de algoritmos cuánticos parametrizados dentro de una arquitectura de microservicios corporativa**. 

Esta infraestructura demuestra cómo una Unidad de Procesamiento Cuántico (QPU) —simulada localmente de forma offline— opera como un coprocesador acelerador asíncrono y desacoplado. Se establecen las bases de **Quantum-As-A-Service (QaaS)** mediante el empaquetado en contenedores Linux, garantizando alta disponibilidad a través de la orquestación en Kubernetes (Colima) y eliminando las malas prácticas de credenciales hardcodeadas mediante la inyección en caliente de **Kubernetes Secrets** y la validación stateless con **JSON Web Tokens (JWT)**.

---

## 🗺️ 1. Diagrama Arquitectónico por Capas (Multi-Tier Architecture)

La infraestructura se divide estrictamente en 4 capas de abstracción para aislar las responsabilidades de red, gobernanza, lógica web y procesamiento físico matricial:

```text
========================================================================================
 CAPA 1: RED INTERNA / PERÍMETRO PÚBLICO (Frontera de Entrada Clásica)
========================================================================================
  [ CLIENTE / CURL ] ────( HTTP POST /api/v1/... )────► [ PUERTO LOCAL 9000 ]
                                                                 │
                                    Mapea mediante Port-Forward  │
                                                                 ▼
========================================================================================
 CAPA 2: GOBERNANZA E INFRAESTRUCTURA DE RED (Service Mesh & Ingress Native Layer)
========================================================================================
  ┌──────────────────────────────────────────────────────────────────────────────────┐
  │ ☸️ KUBERNETES INGRESS CONTROLLER (Frontera de Control Local - Plano de Datos)    │
  │  • Intercepta las llamadas del puerto seguro 9000 sin tocar la IP de la Mac.     │
  │  • Actúa como el balanceador primario de la red virtual del clúster.             │
  └────────────────────────────────────────┬─────────────────────────────────────────┘
                                           │ Enrutamiento Interno Inmune a Firewalls
                                           ▼
========================================================================================
 CAPA 3: SERVICIOS, AUTENTICACIÓN Y DISPONIBILIDAD (Container Web App Layer)
========================================================================================
  ┌──────────────────────────────────────────────────────────────────────────────────┐
  │ ☸️ KUBERNETES DEPLOYMENT BALANCER (api-cuantica-service:5000)                    │
  │  • Distribuye el payload balanceando la carga entre las 2 réplicas activas.      │
  └─────────────────────┬──────────────────────────────────────┬─────────────────────┘
                        │ (Balanceo Round-Robin Nativo)        │
                        ▼                                      ▼
           ┌──────────────────────────┐           ┌──────────────────────────┐
           │   📦 POD 01 (Gunicorn)   │           │   📦 POD 02 (Gunicorn)   │
           ├──────────────────────────┤           ├──────────────────────────┤
           │ • Valida Firma JWT       │           │ • Valida Firma JWT       │
           │ • Lee Secretos en RAM    │           │ • Lee Secretos en RAM    │
           └────────────┬─────────────┘           └────────────┬─────────────┘
                        │                                      │
========================================================================================
 CAPA 4: CO-PROCESAMIENTO ACELERADOR (Quantum Core Compute Layer)
========================================================================================
                        │ Inyecta Escalar Real (Radianes)      │
                        ▼                                      ▼
           ┌──────────────────────────┐           ┌──────────────────────────┐
           │  PENNYLANE SIMULATOR     │           │  PENNYLANE SIMULATOR     │
           │  (default.qubit 2Q)      │           │  (default.qubit 2Q)      │
           │  Altera e^-iθ y matrices │           │  Altera e^-iθ y matrices │
           └──────────────────────────┘           └──────────────────────────┘
```

---

## 📥 2. Especificación de Contratos de Endpoints (API Contract)

### **A. Intercambio de Credenciales (Login)**
### **POST** `/api/v1/auth/login`
Valida las identidades contra la contraseña inyectada en caliente desde la bóveda de secretos y emite un token firmado criptográficamente válido por 15 minutos.

* **Payload de Entrada (JSON):**
```json
{
  "usuario": "desarrollador-cuantico",
  "contrasena": "password123"
}
```
* **Respuesta del Servidor (200 OK):**
```json
{
  "token_acceso_jwt": "eyJhbGciOiJIUzI1NiIsInR5..."
}
```

---

### **B. Procesamiento del Circuito Cuántico**
### **POST** `/api/v1/quantum/procesar`
Exige el token JWT emitido dentro de la cabecera estándar de autorización. Recibe un parámetro en grados sexagesimales clásicos, los transforma a radianes e induce un entrelazamiento de partículas en la Esfera de Bloch.

* **Cabecera Requerida:** `Authorization: Bearer <TU_JWT>`
* **Payload de Entrada (JSON):**
```json
{
  "id_solicitud": "PROD-JWT-VERIFICADO-OK",
  "angulo_grados": 90.0
}
```
* **Respuesta del Servidor (200 OK):**
```json
{
  "angulo_procesado_rad": 1.5708,
  "distribucion_de_probabilidad": {
    "00": "50.00%",
    "01": "0.00%",
    "10": "0.00%",
    "11": "50.00%"
  },
  "estado_mas_probable": "00",
  "id_solicitud": "PROD-JWT-VERIFICADO-OK",
  "operador_autorizado": "desarrollador-cuantico"
}
```

## ⚛️ 3. Plano Técnico del Circuito Cuántico (Circuito de Bell Parametrizado)

Este es el esquema de compuertas lógicas cuánticas que se ejecuta de forma síncrona en la memoria RAM del contenedor al pasar la barrera del JWT:

```text
               📥 ENTRADA                ⚙️ PROCESAMIENTO                📤 SALIDA
        (Estado Base Clásico)      (Superposición / Rotación)     (Colapso Probabilístico)

           |0⟩ ───────────────[ H ]───────────[ RX(θ) ]───────■───────────[ M ]───► 50% |00⟩
                                                              │

           |0⟩ ───────────────────────────────────────────────X───────────[ M ]───► 50% |11⟩
                                                                            
                                                            [CNOT]
                                                    (Control: Q0 / Target: Q1)
```
* *Nota Física:* Al alimentar al motor con 90° (π/2 rad) seguido de una interacción de espín mediante una compuerta `CNOT`, las amplitudes de probabilidad colapsan en un **Estado de Bell de correlación máxima**, provocando un entrelazamiento cuántico puro donde los estados mixtos (`01` y `10`) tienen un 0% absoluto de probabilidad de manifestarse.

---

## 📁 Estructura General del Repositorio
El código fuente de la aplicación web y los Hamiltonianos de simulación física cuántica se encuentran estrictamente desacoplados de los manifiestos de orquestación de infraestructura, utilizando `ConfigMaps` para montar la lógica caliente de red:

```text
api_cuantica_local/
│
├── requirements.txt         # Dependencias rígidas de producción (Flask, PennyLane, Gunicorn, PyJWT)
├── Dockerfile               # Instrucciones de empaquetado optimizadas con caché de capas
├── run.py                   # Punto de entrada minimalista del servidor Gunicorn WSGI
├── README.md                # Documentación técnica del portafolio (Este archivo)
│
├── src/                     # CÓDIGO FUENTE ULTRA-DOCUMENTADO
│   ├── __init__.py          # Fábrica de Aplicaciones (App Factory Pattern)
│   ├── routes.py            # Capa de Red: Validación Stateless JWT y Type Hinting
│   └── quantum_engine.py    # Capa Lógica: Hardware virtual y circuitos parametrizados
│
└── k8s_infra/               # CAPA DE INFRAESTRUCTURA Y DEVSECOPS OFFLINE
    ├── 01-infraestructura.yaml    # Deployment (Volúmenes en caliente) y Service balanceador
    ├── 02-secrets.yaml            # 🔐 Bóveda Opaque con firmas y passwords cifrados en Base64
    └── 03-routes-config.yaml      # ConfigMap con inyección dinámica de código en RAM
```

---

## 🚀 Secuencia de Orquestación y Pruebas Locales (Modo Offline)

Para levantar la infraestructura de forma segura en tu entorno local con **Colima** limpiando sockets de memoria previos, sigue esta secuencia ordenada:

```bash
# 1. Compilar la imagen base bajo el kernel del clúster
export DOCKER_HOST="unix://\$HOME/.colima/default/docker.sock"
docker build -t api-cuantica-modular-img:latest .

# 2. Lanzar la orquestación masiva de infraestructura y secretos de estado
kubectl apply -f k8s_infra/

# 3. Mitigación DevOps: Forzar recreación destructiva para limpiar hilos de memoria
kubectl delete pods -l app=api-cuantica
kill -9 \$(lsof -t -i:9000) 2>/dev/null || true

# 4. Abrir el puente de red virtual entre la Mac y el clúster
kubectl port-forward service/api-cuantica-service 9000:5000
```

### 📡 Pruebas de Humo de Extremo a Extremo (E2E Tests)
1. **Paso A: Obtención del JWT Firmado:**
```bash
curl -s -X POST http://localhost:9000/api/v1/auth/login \
     -H "Content-Type: application/json" \
     -d '{"usuario": "desarrollador-cuantico", "contrasena": "password123"}'
```
2. **Paso B: Consumo del Circuito Cuántico:** Envíe el token resultante en la cabecera `Authorization`:
```bash
curl -i -X POST http://localhost:9000/api/v1/quantum/procesar \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <COPIA_AQUÍ_EL_JWT>" \
     -d '{"id_solicitud": "E2E-JWT-OK", "angulo_grados": 90.0}'
```
