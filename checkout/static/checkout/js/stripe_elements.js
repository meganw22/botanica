/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Ensure jQuery is loaded and available before this script runs
$(document).ready(function () {
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
    var card = elements.create('card', { style: style });
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
        form.addEventListener('submit', function (ev) {
            ev.preventDefault();
            card.update({ 'disabled': true });
            submitButton.setAttribute('disabled', true);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);

            // From using {% csrf_token %} in the form
            var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            var postData = {
                'csrfmiddlewaretoken': csrfToken,
                'client_secret': clientSecret,
            };

            var url = '/checkout/cache_checkout_data/';

            $.post(url, postData).done(function () {
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: $.trim(form.customer_name.value),
                            phone: $.trim(form.phone_number.value),
                            email: $.trim(form.email_address.value),
                            address: {
                                line1: $.trim(form.street_address1.value),
                                line2: $.trim(form.street_address2.value),
                                city: $.trim(form.town_or_city.value),
                                country: $.trim(form.country.value),
                            }
                        }
                    },
                    shipping: {
                        name: $.trim(form.customer_name.value),
                        phone: $.trim(form.phone_number.value),
                        address: {
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            postal_code: $.trim(form.postcode.value),
                            country: $.trim(form.country.value),
                        }
                    }
                }).then(function (result) {
                    if (result.error) {
                        // Display error message
                        var errorDiv = document.getElementById('card-errors');
                        var html = `
                            <span class="icon" role="alert">
                            <i class="fas fa-times"></i>
                            </span>
                            <span>${result.error.message}</span>`;
                        errorDiv.innerHTML = html;
                        $('#payment-form').fadeToggle(100);
                        $('#loading-overlay').fadeToggle(100);
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
            }).fail(function () {
                location.reload();
            });
        });
    } else {
        console.error('Form or submit button not found.');
    }
});