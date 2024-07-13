# ecommerce_platform/orders/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

DATABASE_URL = "postgresql://postgres:12345@db/orders_db"


class Order(BaseModel):
    id: int
    cart_id: int
    total_price: float


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn


@app.get("/orders", response_model=List[Order])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders


@app.post("/orders", response_model=Order)
def create_order(order: Order):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (cart_id, total_price) VALUES (%s, %s) RETURNING *",
                   (order.cart_id, order.total_price))
    new_order = cursor.fetchone()
    conn.commit()
    conn.close()
    return new_order


@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
    order = cursor.fetchone()
    conn.close()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order: Order):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET cart_id = %s, total_price = %s WHERE id = %s RETURNING *",
                   (order.cart_id, order.total_price, order_id))
    updated_order = cursor.fetchone()
    conn.commit()
    conn.close()
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order


@app.delete("/orders/{order_id}", response_model=dict)
def delete_order(order_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE id = %s RETURNING id", (order_id,))
    deleted_id = cursor.fetchone()
    conn.commit()
    conn.close()
    if deleted_id is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}
