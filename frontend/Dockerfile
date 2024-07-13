# ecommerce_platform/frontend/Dockerfile

FROM nginx:alpine

COPY ./templates /usr/share/nginx/html/templates
COPY ./static /usr/share/nginx/html/static
COPY ./index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
