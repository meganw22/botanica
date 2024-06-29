// ----------------------------------------- base.html

// Search Bar Validation
function validateSearchForm(form) {
    var searchInput = form.querySelector('#searchInput').value.trim();
    if (searchInput === '') {
        alert('Please enter a search term.');
        return false;
    }
    return true;
}

// -----------------------------------product_detail.html

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
    var price = parseFloat(prices[height]) || parseFloat(prices.smallest);
    document.getElementById('priceDisplay').innerText = price.toFixed(2);
}

function validateForm(event) {
    var selectedHeight = document.getElementById('selected-height-input').value;
    if (!selectedHeight) {
        event.preventDefault();
        alert('Please select a height for your plant.');
    }
}

// Quantity Selectors
function decreaseQuantity(button) {
    var quantityInput = button.nextElementSibling;
    var currentValue = parseInt(quantityInput.value);
    if (currentValue > 1) {
        quantityInput.value = currentValue - 1;
    } else {
        alert("Quantity cannot be less than 1.");
    }
    updateQuantity(quantityInput);
}

function increaseQuantity(button) {
    var quantityInput = button.previousElementSibling;
    var currentValue = parseInt(quantityInput.value);
    if (currentValue < 99) {
        quantityInput.value = currentValue + 1;
    } else {
        alert("Quantity cannot be more than 99.");
    }
    updateQuantity(quantityInput);
}

function updateQuantity(input) {
    var value = parseInt(input.value);
    if (isNaN(value) || value < 1) {
        alert("Quantity must be a number between 1 and 99.");
        input.value = 1;
    } else if (value > 99) {
        alert("Quantity must be a number between 1 and 99.");
        input.value = 99;
    }
    document.getElementById('quantity-input').value = input.value;
}

// Show inital price value as smallest price available
document.addEventListener("DOMContentLoaded", function () {
    updateFormInputs();
    var initialHeight = document.getElementById('selected-height-input').value || 'sm';
    updatePriceDisplay(initialHeight);
});
