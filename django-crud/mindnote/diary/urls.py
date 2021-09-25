from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 메인 페이지
    path('diary/', views.PageListView.as_view(), name="page-list"), # 일기 목록 
    path('diary/info/', views.info, name="info"), # 감정 일기에 대한 설명
    path('diary/write/', views.PageCreateView.as_view(), name="page-create"), # 새로운 일기 작성
    path('diary/page/<int:pk>/', views.PageDetailView.as_view(), name="page-detail"), # 각각의 일기 내용
    path('diary/page/<int:pk>/edit/', views.PageUpdateView.as_view(), name="page-update"), # 각각의 일기 수정
    path('diary/page/<int:pk>/delete/', views.PageDeleteView.as_view(), name="page-delete"), # 각각의 일기 삭제
]
