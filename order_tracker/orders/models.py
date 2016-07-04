from __future__ import unicode_literals

from django.db import models

# Create your models here.

# The following models represent physical items which are in our inventory
# and the inventory itself

class Component(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Inventory(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class InventoryItem(models.Model):
	inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
	component = models.ForeignKey(Component, on_delete=models.CASCADE)
	number = models.IntegerField()

	def __str__(self):
		return self.component.name

# The following models represent the more "virtual" concepts of a products
# pricing, customers and orders.

class Product(models.Model):
	"""Representative of something sold to a customer.
	A Product consists of a single component (which of course can be made of
	multiple subcomponents)
	"""
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class ProductComponent:
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	component = models.ForeignKey(Component, on_delete=models.CASCADE)

class PricingModel(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class PricingModelPrice(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	model   = models.ForeignKey(PricingModel, on_delete=models.CASCADE)
	price   = models.DecimalField(max_digits=9, decimal_places=2)

class Customer(models.Model):
	name = models.CharField(max_length=200)
	pricingModel = models.ForeignKey(PricingModel, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class CustomerOrder(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	date = models.DateTimeField('date of order')
	
class CustomerOrderItem(models.Model):
	order = models.ForeignKey(Customer, on_delete=models.CASCADE)

# The following represent suppliers from which we can buy components
# To add to our inventory

class Supplier(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class SupplierComponent(models.Model):
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	component = models.ForeignKey(Component, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	
class SupplierOrder(models.Model):
	time = models.DateTimeField('date of order')

class SupplierOrderItem(models.Model):
	order = models.ForeignKey(SupplierOrder, on_delete=models.CASCADE)
	item = models.ForeignKey(SupplierComponent, on_delete=models.CASCADE)

# Components can be build from other components

class ComponentPlan(models.Model):
	component = models.ForeignKey(Component, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.component.name

class SubComponent(models.Model):
	plan = models.ForeignKey( ComponentPlan, on_delete=models.CASCADE)
	component = models.ForeignKey( Component, on_delete=models.CASCADE)
	number = models.IntegerField();
