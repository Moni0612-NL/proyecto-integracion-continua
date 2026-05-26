from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__)

# conexión a postgres
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_NAME = "proyecto_db"
DB_HOST = "db"
DB_PORT = "5432"

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# tabla ejemplo
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    return {
        "mensaje": "API funcionando con Docker y PostgreSQL 🚀"
    }


@app.route("/productos")
def productos():
    lista = Producto.query.all()

    datos = []

    for producto in lista:
        datos.append({
            "id": producto.id,
            "nombre": producto.nombre
        })

    return jsonify(datos)


def esperar_db():
    while True:
        try:
            with app.app_context():
                db.create_all()

                if Producto.query.count() == 0:
                    producto1 = Producto(nombre="Camiseta Docker")
                    producto2 = Producto(nombre="Camiseta Flask")

                    db.session.add(producto1)
                    db.session.add(producto2)
                    db.session.commit()

            print("Base de datos conectada")
            break

        except Exception as e:
            print("Esperando base de datos...")
            time.sleep(3)


if __name__ == "__main__":
    esperar_db()
    app.run(host="0.0.0.0", port=5000)