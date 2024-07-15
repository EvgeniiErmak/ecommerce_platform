# ecommerce_platform/cart/main.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI(title="Cart API", description="API для управления корзиной", version="1.0")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345@db/cart_db")

templates = Jinja2Templates(directory="/frontend/templates")


class CartItem(BaseModel):
    id: int
    product_id: int
    quantity: int


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn


@app.get("/cart", response_model=List[CartItem])
def get_cart():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cart")
    cart_items = cursor.fetchall()
    conn.close()
    return cart_items


@app.post("/cart", response_model=CartItem)
def add_to_cart(cart_item: CartItem):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cart (product_id, quantity) VALUES (%s, %s) RETURNING *",
                   (cart_item.product_id, cart_item.quantity))
    new_cart_item = cursor.fetchone()
    conn.commit()
    conn.close()
    return new_cart_item


@app.put("/cart/{cart_item_id}", response_model=CartItem)
def update_cart_item(cart_item_id: int, cart_item: CartItem):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE cart SET product_id = %s, quantity = %s WHERE id = %s RETURNING *",
                   (cart_item.product_id, cart_item.quantity, cart_item_id))
    updated_cart_item = cursor.fetchone()
    conn.commit()
    conn.close()
    if updated_cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return updated_cart_item


@app.delete("/cart/{cart_item_id}", response_model=dict)
def delete_cart_item(cart_item_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE id = %s RETURNING id", (cart_item_id,))
    deleted_id = cursor.fetchone()
    conn.commit()
    conn.close()
    if deleted_id is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return {"message": "Cart item deleted successfully"}


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request, "message": "Cart service is running"})
