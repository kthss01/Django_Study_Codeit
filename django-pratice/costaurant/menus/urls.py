# cosaurant/menus/urls.py
from django.urls import path
# view를 import 
from . import views

urlpatterns = [
    # path('URL 패턴', view 함수)
    path('', views.index_view)
]
