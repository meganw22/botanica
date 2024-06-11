from django import forms
from .models import Order, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street_address1',
            'street_address2',
            'town_city',
            'county',
            'postcode',
            'country',
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'email_address',
            'contact_number',
        ]

    shipping_address = AddressForm()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_name': 'Full Name',
            'email_address': 'Email Address',
            'contact_number': 'Phone Number',
        }

        self.fields['customer_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False