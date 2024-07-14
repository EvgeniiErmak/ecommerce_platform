# ecommerce_platform/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import os
import psycopg2


# Инициализация баз данных
def init_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345", host="db", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'products_db'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute('CREATE DATABASE products_db')
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'cart_db'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute('CREATE DATABASE cart_db')
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'orders_db'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute('CREATE DATABASE orders_db')
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'payments_db'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute('CREATE DATABASE payments_db')
    cursor.close()
    conn.close()


# Печать информации о текущей директории и файлах
print(f"Current working directory: {os.getcwd()}")
print(f"Templates directory: {os.path.abspath('frontend/templates')}")
print(f"Files in templates directory: {os.listdir('frontend/templates')}")

# Инициализация баз данных
init_db()

# Инициализация FastAPI
app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/products", response_class=HTMLResponse)
async def products(request: Request):
    return templates.TemplateResponse("products.html", {"request": request})


@app.get("/cart", response_class=HTMLResponse)
async def cart(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})


@app.get("/orders", response_class=HTMLResponse)
async def orders(request: Request):
    return templates.TemplateResponse("orders.html", {"request": request})


@app.get("/payments", response_class=HTMLResponse)
async def payments(request: Request):
    return templates.TemplateResponse("payments.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
