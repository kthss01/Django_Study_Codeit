from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloView(request):
    return HttpResponse("<h1>정답입니다!</h1>")