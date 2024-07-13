// ecommerce_platform/frontend/static/js/orders.js

async function fetchOrders() {
    const response = await fetch('http://localhost:8002/orders');
    const orders = await response.json();
    const ordersList = document.getElementById('orders-list');
    ordersList.innerHTML = '';
    orders.forEach(order => {
        const li = document.createElement('li');
        li.classList.add('list-group-item');
        li.textContent = `ID заказа: ${order.id}, ID корзины: ${order.cart_id}, Общая цена: ${order.total_price}`;
        ordersList.appendChild(li);
    });
}

fetchOrders();
