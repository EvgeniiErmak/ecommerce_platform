#!/bin/bash

# ecommerce_platform/scripts/init_cart_db.sh

set -e
echo "Initializing cart_db"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT 'CREATE DATABASE cart_db'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'cart_db')\gexec
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "cart_db" <<-EOSQL
    CREATE TABLE IF NOT EXISTS cart (
        id SERIAL PRIMARY KEY,
        product_id INT NOT NULL,
        quantity INT NOT NULL
    );
EOSQL
