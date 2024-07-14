#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE products_db;
    CREATE DATABASE cart_db;
    CREATE DATABASE orders_db;
    CREATE DATABASE payments_db;
EOSQL
