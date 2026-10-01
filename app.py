# Proyecto: Café Aroma - prototipo web modular con Flask
# Asignatura: Fundamentos de programación web - UNIMINUTO

from flask import Flask, render_template

# Creamos la aplicación
app = Flask(__name__)


# Ruta de la página de inicio
@app.route("/")
def inicio():
    return render_template("index.html")


# Ruta de la página de servicios
@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


# Ruta de la página de contacto
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


# Ejecutamos el servidor en modo debug
if __name__ == "__main__":
    app.run(debug=True)
