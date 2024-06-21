from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total',)
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

    list_display = ('order_id', 'customer_name', 'email_address', 
                    'phone_number', 'date_created', 'total_cost', 
                    'final_amount')
    search_fields = ('order_id', 'customer_name', 'email_address', 
                    'address__phone_number')
    readonly_fields = ('order_id', 'date_created', 'total_cost', 
                    'final_amount')

    def save_model(self, request, obj, form, change):
        if not obj.order_id:
            obj.order_id = obj._generate_order_id()
        super().save_model(request, obj, form, change)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'product_size', 'quantity_ordered', 'item_total')
    search_fields = ('order__order_id', 'product__name', 'product_size')
