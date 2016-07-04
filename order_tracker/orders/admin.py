from django.contrib import admin

from .models import Supplier, Component

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Component)
