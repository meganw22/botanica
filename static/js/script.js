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