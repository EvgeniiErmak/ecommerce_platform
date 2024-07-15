# ecommerce_platform/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import os
import psycopg2


def create_tables(dbname):
    conn = psycopg2.connect(dbname=dbname, user="postgres", password="12345", host="localhost", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()

    # Определение SQL запросов для создания таблиц
    tables = {
        "products_db": """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            description TEXT,
            price DECIMAL
        );
        """,
        "cart_db": """
        CREATE TABLE IF NOT EXISTS cart (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            product_id INTEGER,
            quantity INTEGER
        );
        """,
        "orders_db": """
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            total_price DECIMAL
        );
        """,
        "payments_db": """
        CREATE TABLE IF NOT EXISTS payments (
            id SERIAL PRIMARY KEY,
            order_id INTEGER,
            payment_date TIMESTAMP,
            amount DECIMAL
        );
        """
    }

    # Выполнение SQL запросов для создания таблиц
    if dbname in tables:
        cursor.execute(tables[dbname])

    cursor.close()
    conn.close()


# Инициализация баз данных
def init_db():
    try:
        connection_string = "dbname='postgres' user='postgres' password='12345' host='localhost' port='5432'"
        print(f"Connecting to database with: {connection_string}")
        conn = psycopg2.connect(connection_string)
        conn.autocommit = True
        cursor = conn.cursor()

        # Проверка и создание базы данных
        databases = ['products_db', 'cart_db', 'orders_db', 'payments_db']
        for db in databases:
            cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db}'")
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(f'CREATE DATABASE {db}')
                print(f"Database {db} created successfully.")
            else:
                print(f"Database {db} already exists.")

            # Создание таблиц в базе данных
            create_tables(db)

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")


# Печать информации о текущей директории и файлах
print(f"Current working directory: {os.getcwd()}")
print(f"Templates directory: {os.path.abspath('frontend/templates')}")
print(f"Files in templates directory: {os.listdir('frontend/templates')}")

# Инициализация FastAPI
app = FastAPI(title="E-commerce Platform API", description="API для управления платформой электронной коммерции", version="1.0")

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

    init_db()
    uvicorn.run(app, host="127.0.0.1", port=8000)
