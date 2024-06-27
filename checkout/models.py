from django.db import models
from products.models import Product, PlantPrice
from user_profile.models import Address, UserProfile
from decimal import Decimal
import shortuuid
from django.conf import settings
from django.db.models import Sum


class Order(models.Model):
    """
    Model representing a customer's order
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_id = models.CharField(
        max_length=15, null=False, editable=False, unique=True)
    customer_name = models.CharField(
        max_length=50, null=False, blank=False)
    email_address = models.EmailField(
        max_length=254, null=False, blank=False)
    phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    address = models.OneToOneField(
        Address, null=True, blank=True, on_delete=models.SET_NULL)
    delivery_fee = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    total_cost = models.DecimalField(
        max_digits=15, decimal_places=2, null=False, default=0)
    final_amount = models.DecimalField(
        max_digits=15, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False)

    def _generate_order_id(self):
        """Generate a unique order ID using ShortUUID."""
        return shortuuid.uuid()[:8].upper()

    def update_totals(self):
        """Update the total cost and final amount of the order."""
        self.total_cost = (
            self.items.aggregate(Sum('item_total'))['item_total__sum'] or
            Decimal('0.00')
        )
        free_delivery_threshold = Decimal(
            settings.FREE_DELIVERY_THRESHOLD)
        standard_delivery_cost = Decimal(
            settings.STANDARD_DELIVERY_COST)
        if self.total_cost < free_delivery_threshold:
            self.delivery_fee = standard_delivery_cost
        else:
            self.delivery_fee = Decimal('0.00')
        self.final_amount = self.total_cost + self.delivery_fee
        self.save()

    def save(self, *args, **kwargs):
        """
        Save method to generate order ID and update user profile.
        """
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)
        if self.customer_name and self.email_address:
            user_profile, created = UserProfile.objects.get_or_create(
                user=self.user)
            if not user_profile.default_address:
                user_profile.default_address = Address.objects.create(
                    phone_number=self.phone_number,
                    street_address1=self.address.street_address1,
                    street_address2=self.address.street_address2,
                    town_or_city=self.address.town_or_city,
                    county=self.address.county,
                    postcode=self.address.postcode,
                    country=self.address.country,
                )
                user_profile.save()

    def __str__(self):
        return f'Order {self.order_id}'


class OrderItem(models.Model):
    """
    Model representing an item in an order.
    """
    order = models.ForeignKey(
        Order, null=False, blank=False, related_name='items',
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(
        max_length=2, null=True, blank=False)
    quantity_ordered = models.PositiveIntegerField()
    item_total = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, null=True,
        blank=False)

    def save(self, *args, **kwargs):
        """
        Save method to calculate item total and update order totals.
        """
        if self.product:
            try:
                price = PlantPrice.objects.get(
                    product=self.product, size=self.product_size).price
                self.item_total = Decimal(price) * self.quantity_ordered
            except PlantPrice.DoesNotExist:
                self.item_total = Decimal('0.00')
        super().save(*args, **kwargs)
        self.order.update_totals()

    def __str__(self):
        return f'Item {self.product.easy_name} for order {self.order.order_id}'
