// ecommerce_platform/frontend/static/js/products.js

async function fetchProducts() {
    const response = await fetch('http://localhost:8000/products');
    const products = await response.json();
    const productsList = document.getElementById('products-list');
    productsList.innerHTML = '';
    products.forEach(product => {
        const li = document.createElement('li');
        li.classList.add('list-group-item');
        li.textContent = `Название: ${product.name}, Описание: ${product.description}, Цена: ${product.price}`;
        productsList.appendChild(li);
    });
}

async function addProduct(event) {
    event.preventDefault();
    const productName = document.getElementById('productName').value;
    const productDescription = document.getElementById('productDescription').value;
    const productPrice = document.getElementById('productPrice').value;

    const response = await fetch('http://localhost:8000/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: productName,
            description: productDescription,
            price: productPrice
        })
    });

    if (response.ok) {
        fetchProducts();
    }
}

document.getElementById('add-product-form').addEventListener('submit', addProduct);

fetchProducts();
