# ecommerce_platform/products/main.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345@db/products_db")

templates = Jinja2Templates(directory="/frontend/templates")


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn


@app.get("/products", response_model=List[Product])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    conn.close()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=Product)
def create_product(product: Product):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price) VALUES (%s, %s, %s) RETURNING *",
                   (product.name, product.description, product.price))
    new_product = cursor.fetchone()
    conn.commit()
    conn.close()
    return new_product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s RETURNING *",
                   (product.name, product.description, product.price, product_id))
    updated_product = cursor.fetchone()
    conn.commit()
    conn.close()
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@app.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s RETURNING id", (product_id,))
    deleted_id = cursor.fetchone()
    conn.commit()
    conn.close()
    if deleted_id is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("products.html", {"request": request, "message": "Products service is running"})
