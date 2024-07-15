// ecommerce_platform/frontend/static/js/cart.js

async function fetchCart() {
    const response = await fetch('http://localhost:8001/cart');
    const cartItems = await response.json();
    const cartList = document.getElementById('cart-list');
    cartList.innerHTML = '';
    cartItems.forEach(item => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        li.textContent = `ID продукта: ${item.product_id}, Количество: ${item.quantity}`;

        const deleteButton = document.createElement('button');
        deleteButton.classList.add('btn', 'btn-danger', 'btn-sm');
        deleteButton.textContent = 'Удалить';
        deleteButton.onclick = async () => {
            await fetch(`http://localhost:8001/cart/${item.id}`, { method: 'DELETE' });
            fetchCart();
        };

        li.appendChild(deleteButton);
        cartList.appendChild(li);
    });
}

document.getElementById('cart-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const productId = document.getElementById('product_id').value;
    const quantity = document.getElementById('quantity').value;
    await fetch('http://localhost:8001/cart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: parseInt(productId), quantity: parseInt(quantity) })
    });
    fetchCart();
});

fetchCart();
