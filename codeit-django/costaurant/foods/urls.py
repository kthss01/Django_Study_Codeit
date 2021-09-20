from django.contrib import admin
from django.urls import path
from . import views # . 같은 디렉토리를 의미

urlpatterns = [
    path('menu/', views.index), # views 모듈에서 index 함수 가져오는거
    path('menu/<int:pk>/', views.food_detail)
] 