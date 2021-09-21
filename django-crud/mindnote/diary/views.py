from django.shortcuts import render
from .models import Page

# Create your views here.

def page_list(request):
    object_list = Page.objects.all()
    context = {'object_list': object_list}
    return render(request, 'diary/page_list.html', context)

def page_detail(request, post_id):
    object = Page.objects.get(id=post_id)
    context = {'object': object}
    return render(request, 'diary/page_detail.html', context)

def info(request):
    return render(request, 'diary/info.html')