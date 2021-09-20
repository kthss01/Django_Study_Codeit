from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from menus.models import Menu

# Create your views here.
def index_view(request):
    today = datetime.now().date()
    
    menus = Menu.objects.all()
    
    context = dict()
    context["date"] = today
    context['menus'] = menus
    
    return render(request, 'menus/index.html', context)

def detail(request, pk):
    
    menu = Menu.objects.get(id=pk)
    
    return render(request, 'menus/detail.html', {'menu' : menu})