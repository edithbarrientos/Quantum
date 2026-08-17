# 🌐 API Cuántica Local - Microservicio Híbrido (QaaS)

Este proyecto implementa una **Arquitectura de Software Híbrida Clásico-Cuántica** utilizando el patrón de diseño *Quantum-As-A-Service (QaaS)*. El microservicio está construido con **Flask**, administrado por procesos de producción de **Gunicorn (WSGI)** y encapsulado dentro de un contenedor **Docker** bajo una red aislada de tipo puente (*bridge*). 

El motor de cómputo cuántico utiliza el simulador local de vectores de estado de **PennyLane (Xanadu)**, ejecutándose de forma 100% local en los hilos del procesador sin tocar conexiones externas.

---

## 🗺️ Arquitectura del Sistema e Infraestructura de Red
La API está diseñada para desacoplar el servidor web clásico del procesamiento de álgebra lineal cuántica, garantizando que el sistema operativo no congele los hilos de ejecución de las matrices complejas.

```text
  [ CLIENTE / MAC LOCAL ] (Petición HTTP vía Curl)
             │  
             │ POST http://localhost:5000/api/v1/quantum/procesar
             ▼
  ┌────────────────────────────────────────────────────────┐
  │         CONTENEDOR DOCKER (Entorno Linux Aislado)      │
  ├────────────────────────────────────────────────────────┤
  │  • Red Puente: red_cuantica_puente                    │
  │  • Servidor Web: Gunicorn (WSGI Standard)              │
  │  • Puerto Seguro: 5000 (Completamente alejado del 80)  │
  │                                                        │
  │  ┌───────────────┐      Instancia en Memoria           │
  │  │   src/routes  │ ───► (Valida JSON Clásico)          │
  │  └───────┬───────┘                                     │
  │          │                                             │
  │          ▼                                             │
  │  ┌───────────────┐      Cálculo Numérico Local         │
  │  │ src/quantum_  │ ───► (Simulador default.qubit)      │
  │  │    engine     │      Genera Estados de Bell de 2Q   │
  │  └───────────────┘                                     │
  └────────────────────────┬───────────────────────────────┘
                           │
                           ▼ Devuelve Inferencia JSON
  [ CLIENTE / MAC LOCAL ] (Muestra Distribución de Probabilidades)
```

---

## 📁 Estructura Modular del Proyecto
El código implementa el **Factory Pattern** (Fábrica de Aplicaciones) y **Flask Blueprints** para aislar las responsabilidades de red de la lógica física cuántica:

```text
api_cuantica_local/
│
├── requirements.txt        # Dependencias rígidas (pennylane, flask, gunicorn, numpy)
├── Dockerfile              # Plano de compilación para entornos Linux de producción
├── run.py                  # Punto de entrada minimalista del servidor
└── src/                    # Módulo principal del código fuente
    ├── __init__.py         # Inicializador y fábrica del microservicio (App Factory)
    ├── routes.py           # Capa de Red: Controladores, endpoints HTTP y parsing JSON
    └── quantum_engine.py   # Capa Lógica: Hardware virtual y circuitos parametrizados
```

---

## 📥 Especificación del Endpoint (API Contract)

### **POST** `/api/v1/quantum/procesar`
Recibe un parámetro clásico en grados y calcula el entrelazamiento y colapso de fases en la Esfera de Bloch.

* **Payload de Entrada (JSON):**
```json
{
  "id_solicitud": "PRODUCCION-DOCKER-OK",
  "angulo_grados": 90.0
}
```

* **Respuesta del Servidor (JSON):**
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
  "id_solicitud": "PRODUCCION-DOCKER-OK"
}
```
*Nota: Al inyectar un ángulo de 90° ($\pi/2$ rad) seguido de un entrelazamiento CNOT, el circuito genera un Estado de Bell de correlación máxima, forzando a los cúbits mixtos (`01` y `10`) a colapsar a 0% de probabilidad.*

---

## 🚀 Despliegue y Orquestación Local
Para levantar el orquestador de contenedores (asegúrate de tener **Colima** o tu daemon de Docker activo) y montar la red puente aislada, ejecuta en tu terminal:

```bash
# 1. Crear la red puente de forma explícita
docker network create --driver bridge red_cuantica_puente

# 2. Compilar la imagen de la API modular
docker build -t api-cuantica-modular-img .

# 3. Lanzar el contenedor en segundo plano amarrado a la red
docker run -d --name api-cuantica-contenedor --network red_cuantica_puente -p 5000:5000 api-cuantica-modular-img
```

## 📡 Pruebas de Humo (Testing de Endpoints)
Puedes interrogar localmente a tu procesador cuántico contenerizado ejecutando el comando de red clásico:

```bash
curl -X POST http://localhost:5000/api/v1/quantum/procesar \
     -H "Content-Type: application/json" \
     -d '{"id_solicitud": "TEST-CI-CD", "angulo_grados": 90.0}'
```
