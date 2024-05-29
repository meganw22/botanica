// -----------------------------------product_detail.html

//Quantity Control

var prices = JSON.parse(document.getElementById('prices-data').textContent);

function decreaseQuantity() {
    var quantityInput = document.getElementById('quantity');
    var currentValue = parseInt(quantityInput.value);
    if (currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
    updateFormInputs();
}

function increaseQuantity() {
    var quantityInput = document.getElementById('quantity');
    var currentValue = parseInt(quantityInput.value);
    quantityInput.value = currentValue + 1;
    updateFormInputs();
}

function selectHeight(height) {
    document.getElementById('selected-height-input').value = height;
    updatePriceDisplay(height);
}

function updateFormInputs() {
    document.getElementById('quantity-input').value = document.getElementById('quantity').value;
}

function updatePriceDisplay(height) {
    var price = prices[height] || prices.smallest;
    document.getElementById('priceDisplay').innerText = price;
}

function validateForm(event) {
    var selectedHeight = document.getElementById('selected-height-input').value;
    if (!selectedHeight) {
        event.preventDefault();
        alert('Please select a height for your plant.');
    }
}

// Initialize form inputs
updateFormInputs();
