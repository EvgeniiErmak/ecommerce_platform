#!/bin/bash

# ecommerce_platform/scripts/init_payments_db.sh

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT 'CREATE DATABASE payments_db'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'payments_db')\gexec
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "payments_db" <<-EOSQL
    CREATE TABLE IF NOT EXISTS payments (
        id SERIAL PRIMARY KEY,
        order_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        status VARCHAR(50) NOT NULL
    );
EOSQL
