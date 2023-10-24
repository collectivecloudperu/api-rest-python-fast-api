from fastapi import FastAPI
from typing import Union

app = FastAPI()

from models import Bicicletas
import mysql.connector

mibd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "test"
)

# Listar todos los registros
@app.get("/")
def main():
    return{"Hola": "Mundo"}

# Leer todos los registros
@app.get("/productos")
def listartodo():
    cursor = mibd.cursor()
    cursor.execute("SELECT * FROM bicicletas")
    resultado = cursor.fetchall()
    return{"bicicletas": resultado}

# Crear un registro
@app.post("/productos")
def crear(nombre: str, precio: str, stock: str):
    cursor = mibd.cursor()
    sql = "INSERT INTO bicicletas (nombre, precio, stock) VALUES (%s, %s, %s)"
    val = (nombre, precio, stock)
    cursor.execute(sql, val)
    mibd.commit()
    return {"Registro Creado Correctamente !"}

# Leer un registro
@app.get("/productos/{id}")
def leer(id: int):
    cursor = mibd.cursor()
    cursor.execute(f"SELECT * FROM bicicletas WHERE id = {id}")
    resultado = cursor.fetchone()
    return {"bicicleta": resultado}

# Actualizar un registro
@app.put("/productos/{id}")
def actualizar(item: Bicicletas):
    i = item.id
    n = item.nombre
    p = item.precio
    s = item.stock

    cursor = mibd.cursor()
    sql = "UPDATE bicicletas SET nombre = %s, precio = %s, stock = %s WHERE id = %s" 
    val = (n, p, s, i)
    cursor.execute(sql, val)
    mibd.commit()
    return ("Registro Actualizado Correctamente !")

# Eliminar un registro
@app.delete("/productos/{id}")
def eliminar(id: int):
    cursor = mibd.cursor()
    cursor.execute(f"DELETE FROM bicicletas WHERE id = {id}")
    mibd.commit()
    return {"Registro Eliminado Correctamente !"}