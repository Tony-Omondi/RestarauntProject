from django.shortcuts import render
from . models import Menu

# Create your views here.
def index(request):
    return render(request, 'hotel/index.html', {})

def menu_view(request):
    items = Menu.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})