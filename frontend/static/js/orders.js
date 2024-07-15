// ecommerce_platform/frontend/static/js/orders.js

async function fetchOrders() {
    const response = await fetch('http://localhost:8002/orders');
    const orders = await response.json();
    const ordersList = document.getElementById('orders-list');
    ordersList.innerHTML = '';
    orders.forEach(order => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        li.textContent = `ID продукта: ${order.product_id}, Количество: ${order.quantity}`;

        const deleteButton = document.createElement('button');
        deleteButton.classList.add('btn', 'btn-danger', 'btn-sm');
        deleteButton.textContent = 'Удалить';
        deleteButton.onclick = async () => {
            await fetch(`http://localhost:8002/orders/${order.id}`, { method: 'DELETE' });
            fetchOrders();
        };

        li.appendChild(deleteButton);
        ordersList.appendChild(li);
    });
}

document.getElementById('orders-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const productId = document.getElementById('product_id').value;
    const quantity = document.getElementById('quantity').value;
    await fetch('http://localhost:8002/orders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: parseInt(productId), quantity: parseInt(quantity) })
    });
    fetchOrders();
});

fetchOrders();
