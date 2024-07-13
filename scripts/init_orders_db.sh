#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        cart_id INT NOT NULL,
        total_price NUMERIC NOT NULL
    );
EOSQL
