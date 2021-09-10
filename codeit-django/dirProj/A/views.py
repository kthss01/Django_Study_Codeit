from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html') # 샌드위치 구조로 A/index.html로 해야함