from django.contrib import admin

from .models import Component, Inventory, InventoryItem
from .models import Product, Customer, PricingModel
from .models import Supplier

# Register your models here.
admin.site.register(Component)
admin.site.register(Inventory)
admin.site.register(InventoryItem)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(PricingModel)
