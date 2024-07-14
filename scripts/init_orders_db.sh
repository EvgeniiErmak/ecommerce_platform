#!/bin/bash

# ecommerce_platform/scripts/init_orders_db.sh

set -e
echo "Initializing orders_db"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT 'CREATE DATABASE orders_db'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'orders_db')\gexec
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "orders_db" <<-EOSQL
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        cart_id INT NOT NULL,
        total_price DECIMAL(10, 2) NOT NULL
    );
EOSQL
