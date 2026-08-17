FROM python:3.12-slim

WORKDIR /app

# Copiamos e instalamos dependencias de forma masiva
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el punto de entrada y el directorio modular estructurado 'src/'
COPY run.py .
COPY src/ ./src/

EXPOSE 5000

# Arrancamos Gunicorn apuntando al punto de entrada 'run:app' en el puerto 5000 libre
CMD ["gunicorn", "run:app", "-w", "2", "-b", "0.0.0.0:5000", "--timeout", "60"]
