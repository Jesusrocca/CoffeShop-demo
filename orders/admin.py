from django.contrib import admin

# Register your models here.
from .models import Order, OrderProduct

class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInlineAdmin
    ]

admin.site.register(Order, OrderAdmin)