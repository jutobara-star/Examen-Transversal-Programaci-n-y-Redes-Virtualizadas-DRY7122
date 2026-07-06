from flask import Flask
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)

def crear_bd():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        password TEXT
    )
    """)

    usuarios = [
        ("Juan Tobar", generate_password_hash("juan123")),
        ("Hailyn Tapia", generate_password_hash("hailyn123"))
    ]

    for usuario in usuarios:
        cursor.execute(
            "INSERT INTO usuarios(nombre,password) VALUES(?,?)",
            usuario
        )

    conexion.commit()
    conexion.close()

@app.route("/")
def inicio():
    return "Servidor funcionando correctamente."

if __name__ == "__main__":
    crear_bd()
    app.run(host="0.0.0.0", port=7500)
