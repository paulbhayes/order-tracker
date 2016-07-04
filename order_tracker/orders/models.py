from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Supplier(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Component(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class SupplierComponent(models.Model):
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	component = models.ForeignKey(Component, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=9, decimal_places=2)

	

class Order(models.Model):
	time = models.DateTimeField('date of order')

class OrderItem(models.Model):
	item = models.ForeignKey(SupplierComponent, on_delete=models.CASCADE)
