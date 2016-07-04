from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Inventory, InventoryItem

# Create your views here.
def index(request):
	return HttpResponse("Hello, world (orders index)")

def inventory(request):
	name = 'default'
	inventory = Inventory.objects.get(name=name)
	inventory = get_object_or_404(Inventory, name=name)
	context = {'inventory' : inventory}
	return render(request, 'orders/inventory.html', context)
