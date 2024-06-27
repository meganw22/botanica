from django import forms
from .models import Order
from user_profile.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'county',
            'postcode',
            'country',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number *',
            'street_address1': 'Street Address 1 *',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town/City *',
            'county': 'County *',
            'postcode': 'Postcode *',
            'country': 'Country *',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = (
                placeholders[field]
                )
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        self.fields['phone_number'].required = True
        self.fields['street_address1'].required = True
        self.fields['street_address2'].required = False
        self.fields['town_or_city'].required = True
        self.fields['county'].required = True
        self.fields['postcode'].required = True
        self.fields['country'].required = True


class OrderForm(forms.ModelForm):
    address = AddressForm()

    class Meta:
        model = Order
        fields = [
            'customer_name',
            'email_address',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_name': 'Full Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
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
