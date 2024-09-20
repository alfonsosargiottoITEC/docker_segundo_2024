import os

from dotenv import load_dotenv
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)

from forms import MarcaForm

app = Flask(__name__)

# Configuracion de SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import Marca, Tipo, User, Vehiculo
from repositories.marca_repository import MarcaRepository
from services.marca_service import MarcaService

load_dotenv()


@app.route("/users", methods=["POST"])
def user():
    data = request.get_json()
    username = data.get("nombre_usuario")
    password = data.get("password")

    password_hasheada = generate_password_hash(
        password=password,
        method="pbkdf2",
        salt_length=8,
    )
    print(password_hasheada)
    # try:
    nuevo_usuario = User(username=username, password_hash=password_hasheada)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"Usuario Creado": username}), 201
    # except:
    #    return jsonify({"Error": "Algo salio mal"})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("nombre_usuario")
    password = data.get("password")

    usuario = User.query.filter_by(username=username).first()

    if usuario and check_password_hash(pwhash=usuario.password_hash, password=password):
        return jsonify({"Mensaje": "Usuario Logeado"})
    return jsonify({"Mensaje": "NO MATCH"})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/marca_list", methods=["POST", "GET"])
def marcas():
    formulario = MarcaForm()

    services = MarcaService(MarcaRepository())
    marcas = services.get_all()

    if request.method == "POST":
        nombre = request.form["nombre"]
        services.create(nombre=nombre)
        return redirect(url_for("marcas"))

    return render_template("marca_list.html", marcas=marcas, formulario=formulario)


@app.route("/marca/<id>/vehiculos")
def vehiculos_por_marca(id):
    # vehiculos = Vehiculo.query.filter_by(marca_id=id)
    marca = Marca.query.get_or_404(id)
    vehiculos = marca.vehiculos
    return render_template("vehiculos_by_marca.html", vehiculos=vehiculos, marca=marca)


@app.route("/marca/<id>/editar", methods=["GET", "POST"])
def marca_editar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == "POST":
        marca.nombre = request.form["nombre"]
        db.session.commit()
        return redirect(url_for("marcas"))

    return render_template("marca_edit.html", marca=marca)


@app.route("/tipo_list")
def tipos():
    tipos = Tipo.query.all()
    return render_template("tipo_list.html", tipos=tipos)


@app.route("/vehiculos_list", methods=["POST", "GET"])
def vehiculos():
    vehiculos = Vehiculo.query.all()
    marcas = Marca.query.all()
    tipos = Tipo.query.all()

    if request.method == "POST":
        modelo = request.form["modelo"]
        anio = request.form["anio_fabricacion"]
        precio = request.form["precio"]
        marca = request.form["marca"]
        tipo = request.form["tipo"]
        vehiculo_nuevo = Vehiculo(
            modelo=modelo,
            anio_fabricacion=anio,
            precio=precio,
            marca_id=marca,
            tipo_id=tipo,
        )
        db.session.add(vehiculo_nuevo)
        db.session.commit()
        return redirect(url_for("vehiculos"))

    return render_template(
        "vehiculos_list.html",
        vehiculos=vehiculos,
        marcas=marcas,
        tipos=tipos,
    )
