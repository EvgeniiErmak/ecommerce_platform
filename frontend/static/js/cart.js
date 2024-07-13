// ecommerce_platform/frontend/static/js/cart.js

async function fetchCart() {
    const response = await fetch('http://localhost:8001/cart');
    const cartItems = await response.json();
    const cartList = document.getElementById('cart-list');
    cartList.innerHTML = '';
    cartItems.forEach(item => {
        const li = document.createElement('li');
        li.classList.add('list-group-item');
        li.textContent = `ID продукта: ${item.product_id}, Количество: ${item.quantity}`;
        cartList.appendChild(li);
    });
}

fetchCart();
