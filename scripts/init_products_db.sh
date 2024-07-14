#!/bin/bash

# ecommerce_platform/scripts/init_products_db.sh

set -e
echo "Initializing products_db"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT 'CREATE DATABASE products_db'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'products_db')\gexec
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "products_db" <<-EOSQL
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    );
EOSQL
