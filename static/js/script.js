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

document.addEventListener("DOMContentLoaded", function() {
    updateFormInputs();
    var initialHeight = document.getElementById('selected-height-input').value || 'sm';
    updatePriceDisplay(initialHeight);
});