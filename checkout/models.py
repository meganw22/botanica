import shortuuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product

class Order(models.Model):
    order_id = models.CharField(max_length=15, null=False, editable=False, unique=True)
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=255, null=True, blank=True)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    final_amount = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False)

    def _generate_order_id(self):
        """
        Generate a unique order ID using ShortUUID.
        """
        return shortuuid.uuid()[:8].upper()

    def update_totals(self):
        self.total_cost = self.items.aggregate(Sum('item_total'))['item_total__sum'] or 0
        if self.total_cost < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_fee = self.total_cost * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_fee = 0
        self.final_amount = self.total_cost + self.delivery_fee
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order {self.order_id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=False)
    quantity_ordered = models.PositiveIntegerField()
    item_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=False)

    def save(self, *args, **kwargs):
        if self.product:
            self.item_total = self.product.price * self.quantity_ordered
        super().save(*args, **kwargs)
        self.order.update_totals()

    def __str__(self):
        return f'Item {self.product.easy_name} for order {self.order.order_id}'
