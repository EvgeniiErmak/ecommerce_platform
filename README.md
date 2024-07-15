```markdown
# E-commerce Platform

## Описание

Этот проект представляет собой платформу электронной коммерции, состоящую из нескольких микросервисов, включая управление продуктами, корзиной, заказами и платежами. Платформа построена с использованием FastAPI для микросервисов и PostgreSQL в качестве базы данных.

## Структура проекта

```
ecommerce_platform
├── Dockerfile
├── README.md
├── cart
│   ├── Dockerfile
│   └── main.py
├── docker-compose.yml
├── frontend
│   ├── Dockerfile
│   ├── index.html
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── images
│   │   │   └── background.jpg
│   │   └── js
│   │       ├── cart.js
│   │       ├── orders.js
│   │       ├── payments.js
│   │       └── products.js
│   └── templates
│       ├── base.html
│       ├── cart.html
│       ├── index.html
│       ├── orders.html
│       ├── payments.html
│       └── products.html
├── main.py
├── orders
│   ├── Dockerfile
│   └── main.py
├── payments
│   ├── Dockerfile
│   └── main.go
├── products
│   ├── Dockerfile
│   └── main.py
├── project_structure.txt
├── requirements.txt
├── scripts
│   ├── init_cart_db.sh
│   ├── init_orders_db.sh
│   ├── init_payments_db.sh
│   └── init_products_db.sh
└── tests
    └── test_products.py
```

## Установка и запуск

### Требования

- Docker
- Docker Compose

### Шаги установки

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/ecommerce_platform.git
    cd ecommerce_platform
    ```

2. Создайте и запустите контейнеры Docker:
    ```bash
    docker-compose up --build
    ```

### Доступ к микросервисам

- Главная страница: [http://localhost:8000](http://localhost:8000)
- Сервис продуктов: [http://localhost:8000/products](http://localhost:8000/products)
- Сервис корзины: [http://localhost:8001/cart](http://localhost:8001/cart)
- Сервис заказов: [http://localhost:8002/orders](http://localhost:8002/orders)
- Сервис платежей: [http://localhost:8003/payments](http://localhost:8003/payments)

### Документация API

Документация для каждого микросервиса доступна по следующим URL:

- Продукты: [http://localhost:8000/docs](http://localhost:8000/docs)
- Корзина: [http://localhost:8001/docs](http://localhost:8001/docs)
- Заказы: [http://localhost:8002/docs](http://localhost:8002/docs)
- Платежи: [http://localhost:8003/docs](http://localhost:8003/docs)

## Структура каталогов и файлов

### Корневой каталог

- `Dockerfile`: Основной Dockerfile для сборки образа всего приложения.
- `README.md`: Документация проекта.
- `docker-compose.yml`: Файл для управления контейнерами с помощью Docker Compose.
- `requirements.txt`: Список зависимостей Python для установки через pip.

### Каталог `cart`

- `Dockerfile`: Dockerfile для сервиса корзины.
- `main.py`: Основной файл сервиса корзины, реализующий API.

### Каталог `orders`

- `Dockerfile`: Dockerfile для сервиса заказов.
- `main.py`: Основной файл сервиса заказов, реализующий API.

### Каталог `payments`

- `Dockerfile`: Dockerfile для сервиса платежей.
- `main.go`: Основной файл сервиса платежей, реализующий API.

### Каталог `products`

- `Dockerfile`: Dockerfile для сервиса продуктов.
- `main.py`: Основной файл сервиса продуктов, реализующий API.

### Каталог `frontend`

- `Dockerfile`: Dockerfile для фронтенда.
- `index.html`: Главная страница фронтенда.
- `static/css/style.css`: Стили для фронтенда.
- `static/images/background.jpg`: Фоновое изображение.
- `static/js/cart.js`: JavaScript для страницы корзины.
- `static/js/orders.js`: JavaScript для страницы заказов.
- `static/js/payments.js`: JavaScript для страницы платежей.
- `static/js/products.js`: JavaScript для страницы продуктов.
- `templates/base.html`: Базовый шаблон.
- `templates/cart.html`: Шаблон страницы корзины.
- `templates/index.html`: Шаблон главной страницы.
- `templates/orders.html`: Шаблон страницы заказов.
- `templates/payments.html`: Шаблон страницы платежей.
- `templates/products.html`: Шаблон страницы продуктов.

### Каталог `scripts`

- `init_cart_db.sh`: Скрипт инициализации базы данных корзины.
- `init_orders_db.sh`: Скрипт инициализации базы данных заказов.
- `init_payments_db.sh`: Скрипт инициализации базы данных платежей.
- `init_products_db.sh`: Скрипт инициализации базы данных продуктов.

### Каталог `tests`

- `test_products.py`: Тесты для сервиса продуктов.

## Описание микросервисов

### Сервис продуктов

Сервис для управления продуктами. Реализует следующие конечные точки:

- `GET /products`: Получение списка продуктов.
- `GET /products/{product_id}`: Получение информации о продукте.
- `POST /products`: Добавление нового продукта.
- `PUT /products/{product_id}`: Обновление информации о продукте.
- `DELETE /products/{product_id}`: Удаление продукта.

### Сервис корзины

Сервис для управления корзиной пользователя. Реализует следующие конечные точки:

- `GET /cart`: Получение содержимого корзины.
- `POST /cart`: Добавление товара в корзину.
- `PUT /cart/{cart_item_id}`: Обновление товара в корзине.
- `DELETE /cart/{cart_item_id}`: Удаление товара из корзины.

### Сервис заказов

Сервис для управления заказами. Реализует следующие конечные точки:

- `GET /orders`: Получение списка заказов.
- `GET /orders/{order_id}`: Получение информации о заказе.
- `POST /orders`: Создание нового заказа.
- `PUT /orders/{order_id}`: Обновление заказа.
- `DELETE /orders/{order_id}`: Удаление заказа.

### Сервис платежей

Сервис для управления платежами. Реализует следующие конечные точки:

- `GET /payments`: Получение списка платежей.
- `GET /payments/{payment_id}`: Получение информации о платеже.
- `POST /payments`: Создание нового платежа.
- `PUT /payments/{payment_id}`: Обновление информации о платеже.
- `DELETE /payments/{payment_id}`: Удаление платежа.

```