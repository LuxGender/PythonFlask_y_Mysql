from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL  # importando bd mysql

app = Flask(__name__)

# configurando mysql/conectando a mi bd
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "123456789"
app.config["MYSQL_DB"] = "crud_python"
# ejecutando mysql/inicializando
mysql = MySQL(app)

# configuraciones
app.secret_key = 'misecretkey'


@app.route("/")
def Index():
    return render_template('index.html')

# agrega contacto y crear conexion a bd


@app.route("/add_contact", methods=["POST"])
def add_contact():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        cur = mysql.connection.cursor()  # cur para saber la conexion
        cur.execute('INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)',
                    (nombre, telefono, email))
        mysql.connection.commit()
        flash("Datos ingresado correctamente")
        return redirect(url_for("Index"))

# editar


@app.route("/edit")
def edit_contact():
    return "edit contact"

# eliminar


@app.route("/eliminar")
def eliminar_contact():
    return "eliminar contact"


if __name__ == "__main__":
    app.run(debug=True)
