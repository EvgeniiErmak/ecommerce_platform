// ecommerce_platform/frontend/static/js/orders.js

async function fetchOrders() {
    const response = await fetch('http://localhost:8002/orders');
    const orders = await response.json();
    const ordersList = document.getElementById('orders-list');
    ordersList.innerHTML = '';
    orders.forEach(order => {
        const li = document.createElement('li');
        li.textContent = `Order ID: ${order.id}, Cart ID: ${order.cart_id}, Total Price: ${order.total_price}`;
        ordersList.appendChild(li);
    });
}

fetchOrders();
