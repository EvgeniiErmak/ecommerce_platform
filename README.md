# E-commerce Platform

## Описание

Проект представляет собой платформу электронной коммерции, построенную с использованием микросервисной архитектуры. Каждый микросервис реализует отдельную функциональность, такую как управление продуктами, корзиной, заказами и платежами. Проект использует FastAPI для создания API и Docker для контейнеризации.

## Структура проекта

```plaintext
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

## Установка

### Предварительные требования

- Docker
- Docker Compose
- Python 3.9+
- pip

### Запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-repository-url/ecommerce_platform.git
cd ecommerce_platform
```

2. Установите зависимости Python:

```bash
pip install -r requirements.txt
```

3. Запустите Docker Compose:

```bash
docker-compose up --build
```

Проект будет доступен по адресу `http://localhost:8000`.

## API Документация

Каждый микросервис имеет свою документацию, доступную через Swagger:

- **Главный сервис**: `http://localhost:8000/docs`
- **Сервис корзины**: `http://localhost:8001/docs`
- **Сервис заказов**: `http://localhost:8002/docs`
- **Сервис продуктов**: `http://localhost:8003/docs`
- **Сервис платежей**: `http://localhost:8004/docs`

## Описание микросервисов

### Главный сервис (`main.py`)

Главный сервис отвечает за отображение фронтенда и инициализацию баз данных. Он содержит маршруты для отображения страниц продуктов, корзины, заказов и платежей.

### Сервис корзины (`cart/main.py`)

Сервис корзины управляет товарами в корзине пользователей. Он предоставляет API для получения, добавления, обновления и удаления товаров из корзины.

### Сервис заказов (`orders/main.py`)

Сервис заказов управляет заказами пользователей. Он предоставляет API для получения, создания, обновления и удаления заказов.

### Сервис продуктов (`products/main.py`)

Сервис продуктов управляет информацией о продуктах. Он предоставляет API для получения, создания, обновления и удаления продуктов.

### Сервис платежей (`payments/main.go`)

Сервис платежей управляет платежами пользователей. Он предоставляет API для обработки платежей.

## Пример использования API

### Получение списка продуктов

```bash
curl -X 'GET' \
  'http://localhost:8003/products' \
  -H 'accept: application/json'
```

### Добавление продукта в корзину

```bash
curl -X 'POST' \
  'http://localhost:8001/cart' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "product_id": 1,
  "quantity": 2
}'
```

### Создание заказа

```bash
curl -X 'POST' \
  'http://localhost:8002/orders' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "cart_id": 1,
  "total_price": 100.0
}'
```

### Обработка платежа

```bash
curl -X 'POST' \
  'http://localhost:8004/payments' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "order_id": 1,
  "amount": 100.0
}'
```

## Контакты

Евгений ЕрмакТел.: '+7 930-290-99-80'.

Telegram: '@DJErmak3000'.

LinkedIn: 'www.linkedin.com/in/evgeniiermak'.

Е-mail: `ew.ermak5000@mail.ru`.
