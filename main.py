# ecommerce_platform/main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import psycopg2
from psycopg2 import sql


# Инициализация баз данных и таблиц
def init_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345", host="db", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()

    databases = ['products_db', 'cart_db', 'orders_db', 'payments_db']
    tables = {
        'products_db': """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                price DECIMAL(10, 2) NOT NULL
            );
        """,
        'cart_db': """
            CREATE TABLE IF NOT EXISTS cart (
                id SERIAL PRIMARY KEY,
                product_id INT REFERENCES products(id),
                quantity INT NOT NULL
            );
        """,
        'orders_db': """
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                user_id INT NOT NULL,
                total DECIMAL(10, 2) NOT NULL
            );
        """,
        'payments_db': """
            CREATE TABLE IF NOT EXISTS payments (
                id SERIAL PRIMARY KEY,
                order_id INT REFERENCES orders(id),
                amount DECIMAL(10, 2) NOT NULL,
                status VARCHAR(50) NOT NULL
            );
        """
    }

    for db in databases:
        cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [db])
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db)))

    cursor.close()
    conn.close()

    for db in databases:
        conn = psycopg2.connect(dbname=db, user="postgres", password="12345", host="db", port="5432")
        cursor = conn.cursor()
        cursor.execute(tables[db])
        conn.commit()
        cursor.close()
        conn.close()


# Печать информации о текущей директории и файлах
print(f"Current working directory: {os.getcwd()}")
print(f"Templates directory: {os.path.abspath('frontend/templates')}")
print(f"Files in templates directory: {os.listdir('frontend/templates')}")

# Инициализация FastAPI
app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")


@app.options("/{full_path:path}")
async def preflight(full_path: str, request: Request):
    response = JSONResponse(content={"message": "Preflight CORS"})
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


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
    init_db()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
