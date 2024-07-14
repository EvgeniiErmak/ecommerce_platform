# ecommerce_platform/Dockerfile

FROM postgres:13
COPY ./scripts/init_db.sh /docker-entrypoint-initdb.d/init_db.sh
