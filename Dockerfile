# ecommerce_platform/Dockerfile

FROM postgres:13
COPY ./scripts/init_products_db.sh /docker-entrypoint-initdb.d/init_products_db.sh
COPY ./scripts/init_cart_db.sh /docker-entrypoint-initdb.d/init_cart_db.sh
COPY ./scripts/init_orders_db.sh /docker-entrypoint-initdb.d/init_orders_db.sh
COPY ./scripts/init_payments_db.sh /docker-entrypoint-initdb.d/init_payments_db.sh

# Для FastAPI приложения
FROM python:3.9-slim
WORKDIR /app
COPY ./main.py .
COPY ./frontend ./frontend
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
