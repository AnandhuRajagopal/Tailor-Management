document.addEventListener('DOMContentLoaded', function () {
    const orderId = document.querySelector('#order_id').value;

    const customerMeasurementValues = {
        name: document.querySelector('#name').value,
        measurement: document.querySelector('#measurement').value
    };

    fetch('/measurement/page/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            order_id: orderId,
            ...customerMeasurementValues
        })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data if needed
    })
    .catch(error => {
        // Handle errors if needed
    });
});
