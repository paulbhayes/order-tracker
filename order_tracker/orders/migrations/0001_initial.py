# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date of order')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Component')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='PricingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PricingModelPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PricingModel')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Component')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ComponentPlan')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Component')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='date of order')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.SupplierComponent')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.SupplierOrder')),
            ],
        ),
        migrations.AddField(
            model_name='pricingmodelprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='pricingModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PricingModel'),
        ),
    ]
