FROM python:3.10-slim-bookworm

# 1. Instalar parches de seguridad y compiladores esenciales
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends build-essential gcc g++ make python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Actualizar herramientas base de empaquetado de Python
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3. Copiar e instalar las dependencias nativas de tu malla (Flask, IA, Cripto)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código fuente limpio completo
COPY . .

EXPOSE 5000

# 5. 🚀 ARRANQUE DE PRODUCCIÓN: Pre-carga en RAM + Extensión de Timeout para la IA
CMD ["gunicorn", "run:app", "-w", "2", "--worker-class=gthread", "--threads=4", "--timeout", "120", "--preload", "-b", "0.0.0.0:5000"]
