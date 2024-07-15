// ecommerce_platform/frontend/static/js/cart.js

async function fetchCart() {
    const response = await fetch('http://localhost:8001/cart');
    const cartItems = await response.json();
    const cartList = document.getElementById('cart-list');
    cartList.innerHTML = '';
    cartItems.forEach(item => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        li.innerHTML = `ID продукта: ${item.product_id}, Количество: ${item.quantity}`;

        const updateButton = document.createElement('button');
        updateButton.classList.add('btn', 'btn-warning', 'btn-sm', 'mx-2');
        updateButton.textContent = 'Изменить';
        updateButton.onclick = () => updateCartItem(item.id, item.product_id, item.quantity);

        const deleteButton = document.createElement('button');
        deleteButton.classList.add('btn', 'btn-danger', 'btn-sm');
        deleteButton.textContent = 'Удалить';
        deleteButton.onclick = async () => {
            await fetch(`http://localhost:8001/cart/${item.id}`, { method: 'DELETE' });
            fetchCart();
        };

        li.appendChild(updateButton);
        li.appendChild(deleteButton);
        cartList.appendChild(li);
    });
}

async function addToCart(product_id, quantity) {
    await fetch('http://localhost:8001/cart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: parseInt(product_id), quantity: parseInt(quantity) })
    });
    fetchCart();
}

async function updateCartItem(id, product_id, quantity) {
    const newQuantity = prompt('Введите новое количество:', quantity);
    if (newQuantity !== null) {
        await fetch(`http://localhost:8001/cart/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: product_id, quantity: parseInt(newQuantity) })
        });
        fetchCart();
    }
}

document.getElementById('cart-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const productId = document.getElementById('product_id').value;
    const quantity = document.getElementById('quantity').value;
    await addToCart(productId, quantity);
    document.getElementById('product_id').value = '';
    document.getElementById('quantity').value = '';
});

fetchCart();
