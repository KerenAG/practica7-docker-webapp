from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)

def conectar_db():
    for i in range(5):
        try:
            conexion = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="testdb"
            )
            return conexion
        except:
            time.sleep(3)
    return None

def inicializar_db(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexion.commit()

@app.route('/')
def inicio():
    conexion = conectar_db()

    if conexion:
        inicializar_db(conexion)
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO visitas () VALUES ()")
        conexion.commit()

        cursor.execute("SELECT COUNT(*) FROM visitas")
        total = cursor.fetchone()[0]

        return render_template(
            "index.html",
            total=total,
            estado="Conectado a MySQL correctamente ✅",
            estado_class="ok"
        )
    else:
        return render_template(
            "index.html",
            total=0,
            estado="Error al conectar a MySQL ❌",
            estado_class="error"
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)