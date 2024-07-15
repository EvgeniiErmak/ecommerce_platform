// ecommerce_platform/frontend/static/js/payments.js

async function fetchPayments() {
    const response = await fetch('http://localhost:8003/payments');
    const payments = await response.json();
    const paymentsList = document.getElementById('payments-list');
    paymentsList.innerHTML = '';
    payments.forEach(payment => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        li.textContent = `ID заказа: ${payment.order_id}, Сумма: ${payment.amount}`;

        const deleteButton = document.createElement('button');
        deleteButton.classList.add('btn', 'btn-danger', 'btn-sm');
        deleteButton.textContent = 'Удалить';
        deleteButton.onclick = async () => {
            await fetch(`http://localhost:8003/payments/${payment.id}`, { method: 'DELETE' });
            fetchPayments();
        };

        li.appendChild(deleteButton);
        paymentsList.appendChild(li);
    });
}

document.getElementById('payments-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const orderId = document.getElementById('order_id').value;
    const amount = document.getElementById('amount').value;
    await fetch('http://localhost:8003/payments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ order_id: parseInt(orderId), amount: parseFloat(amount) })
    });
    fetchPayments();
});

fetchPayments();
