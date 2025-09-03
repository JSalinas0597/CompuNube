// frontend/web/static/scriptOrders.js
function getOrders() {
    fetch('http://192.168.80.3:5004/api/orders', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {
        const tbody = document.querySelector('#order-list tbody');
        tbody.innerHTML = '';
        
        data.forEach(order => {
            const row = document.createElement('tr');
            
            // ID
            const idCell = document.createElement('td');
            idCell.textContent = order.id;
            row.appendChild(idCell);
            
            // User Name
            const nameCell = document.createElement('td');
            nameCell.textContent = order.userName;
            row.appendChild(nameCell);
            
            // User Email
            const emailCell = document.createElement('td');
            emailCell.textContent = order.userEmail;
            row.appendChild(emailCell);
            
            // Total Amount
            const totalCell = document.createElement('td');
            totalCell.textContent = order.saleTotal;
            row.appendChild(totalCell);
            
            // Date
            const dateCell = document.createElement('td');
            dateCell.textContent = order.date;
            row.appendChild(dateCell);
            
            // Actions
            const actionsCell = document.createElement('td');
            
            // Edit link
            const editLink = document.createElement('a');
            editLink.href = `/editOrder/${order.id}`;
            editLink.textContent = 'Edit';
            editLink.className = 'btn btn-primary mr-2';
            actionsCell.appendChild(editLink);
            
            // Delete link
            const deleteLink = document.createElement('a');
            deleteLink.href = '#';
            deleteLink.textContent = 'Delete';
            deleteLink.className = 'btn btn-danger';
            deleteLink.addEventListener('click', function() {
                deleteOrder(order.id);
            });
            actionsCell.appendChild(deleteLink);
            
            row.appendChild(actionsCell);
            tbody.appendChild(row);
        });
    })
    .catch(error => console.error('Error:', error));
}

function deleteOrder(orderId) {
    if (confirm('Are you sure you want to delete this order?')) {
        fetch(`http://192.168.80.3:5004/api/orders/${orderId}`, {
            method: 'DELETE',
            credentials: 'include'
        })
        .then(response => response.json())
        .then(data => {
            console.log('Order deleted successfully:', data);
            getOrders(); // Refrescar lista
        })
        .catch(error => console.error('Error:', error));
    }
}
