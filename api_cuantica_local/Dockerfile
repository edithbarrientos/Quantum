# Usamos una imagen oficial y ligera de Python basada en Debian
FROM python:3.12-slim

# Configuramos el directorio de trabajo aislado dentro de Linux
WORKDIR /app

# Copiamos e instalamos los requerimientos de software de golpe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ⚡ COPIADO ESTRUCTURADO:
# Copiamos el archivo de arranque en la raíz y la carpeta modular 'src' con sus subficheros
COPY run.py .
COPY src/ ./src/

# Exponemos el puerto 5000 (totalmente libre de números 80 o variantes)
EXPOSE 5000

# Comando de producción: Arrancamos Gunicorn apuntando al objeto 'app' del archivo 'run'
CMD ["gunicorn", "run:app", "-w", "2", "-b", "0.0.0.0:5000", "--timeout", "60"]
