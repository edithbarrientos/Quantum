from src import create_app

# Creamos la instancia de la aplicación usando el patrón de diseño App Factory
app = create_app()

if __name__ == "__main__":
    # Si se ejecuta de forma directa en desarrollo local, corre en el puerto seguro 5000
    app.run(host="0.0.0.0", port=5000)
