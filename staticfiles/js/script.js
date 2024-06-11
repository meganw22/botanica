// -----------------------------------product_detail.html

// Quantity Control

function decreaseQuantity(button) {
    var quantityInput = button.nextElementSibling;
    var currentValue = parseInt(quantityInput.value);
    if (currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
    updateFormInputs(quantityInput);
}

function increaseQuantity(button) {
    var quantityInput = button.previousElementSibling;
    var currentValue = parseInt(quantityInput.value);
    quantityInput.value = currentValue + 1;
    updateFormInputs(quantityInput);
}

function updateFormInputs(quantityInput) {
    var hiddenInput = quantityInput.closest('form') ? quantityInput.closest('form').querySelector('.quantity-input-hidden') : null;
    if (hiddenInput) {
        hiddenInput.value = quantityInput.value;
    }
}

function updateQuantity(button) {
    var quantityInput = button.previousElementSibling.querySelector('.quantity-input');
    var newValue = quantityInput.value;
    var message = document.getElementById('update-message');
    message.style.display = 'block';
    setTimeout(() => {
        message.style.display = 'none';
    }, 2000);
}


// Select height and show height price

function selectHeight(height) {
    document.getElementById('selected-height-input').value = height;
    updatePriceDisplay(height);
}

function updateFormInputs() {
    var quantity = document.getElementById('quantity').value;
    document.getElementById('quantity-input').value = quantity;
}

function updatePriceDisplay(height) {
    var prices = JSON.parse(document.getElementById('prices-data').textContent);
    console.log('Prices Data:', prices);  // Debug log
    var price = parseFloat(prices[height]) || parseFloat(prices.smallest);
    console.log('Selected Height:', height, 'Price:', price);  // Debug log
    document.getElementById('priceDisplay').innerText = price.toFixed(2);
}

function validateForm(event) {
    var selectedHeight = document.getElementById('selected-height-input').value;
    if (!selectedHeight) {
        event.preventDefault();
        alert('Please select a height for your plant.');
    }
    console.log('Validate Form:', selectedHeight);  // Debug log
}

document.addEventListener("DOMContentLoaded", function() {
    // Initialize form inputs and price display
    updateFormInputs();
    // Pass a default height if available, otherwise use the smallest price
    var initialHeight = document.getElementById('selected-height-input').value || 'sm';
    updatePriceDisplay(initialHeight);
    console.log('DOMContentLoaded: Initialized');  // Debug log
});