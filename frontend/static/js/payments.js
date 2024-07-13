// ecommerce_platform/frontend/static/js/payments.js

async function fetchPayments() {
    const response = await fetch('http://localhost:8003/payments');
    const payments = await response.json();
    const paymentsList = document.getElementById('payments-list');
    paymentsList.innerHTML = '';
    payments.forEach(payment => {
        const li = document.createElement('li');
        li.classList.add('list-group-item');
        li.textContent = `ID платежа: ${payment.id}, Сумма: ${payment.amount}, Статус: ${payment.status}`;
        paymentsList.appendChild(li);
    });
}

fetchPayments();
