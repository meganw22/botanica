document.addEventListener("DOMContentLoaded", function() {
    var stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
    var clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();
    var style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };
    var card = elements.create('card', {style: style});
    card.mount('#card-element');

    // Handle realtime validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            errorDiv.innerHTML = html;
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submit
    var form = document.getElementById('payment-form');
    var submitButton = document.getElementById('submit-button');

    if (form && submitButton) {
        form.addEventListener('submit', function(ev) {
            ev.preventDefault();
            card.update({ 'disabled': true });
            submitButton.setAttribute('disabled', true);

            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                }
            }).then(function(result) {
                if (result.error) {
                    // Display error message
                    var errorDiv = document.getElementById('card-errors');
                    var html = `
                        <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>`;
                    errorDiv.innerHTML = html;

                    card.update({ 'disabled': false });
                    submitButton.removeAttribute('disabled');
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        // Payment succeeded, submit the form
                        var hiddenInput = document.getElementById('id_client_secret_input');
                        hiddenInput.value = clientSecret;
                        form.submit();
                    } else {
                        console.log('PaymentIntent status:', result.paymentIntent.status);
                    }
                }
            });
        });
    } else {
        console.error('Form or submit button not found.');
    }
});
