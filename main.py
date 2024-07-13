# ecommerce_platform/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import os

print(f"Current working directory: {os.getcwd()}")
print(f"Templates directory: {os.path.abspath('frontend/templates')}")
print(f"Files in templates directory: {os.listdir('frontend/templates')}")

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
