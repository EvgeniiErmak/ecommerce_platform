// ecommerce_platform/frontend/static/js/products.js

async function fetchProducts() {
    const response = await fetch('http://localhost:8000/products');
    const products = await response.json();
    const productsList = document.getElementById('products-list');
    productsList.innerHTML = '';
    products.forEach(product => {
        const li = document.createElement('li');
        li.textContent = `Name: ${product.name}, Description: ${product.description}, Price: ${product.price}`;
        productsList.appendChild(li);
    });
}

fetchProducts();
