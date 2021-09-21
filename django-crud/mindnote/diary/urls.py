from django.urls import path
from . import views

urlpatterns = [
    path('diary/', views.page_list, name="page-list"), # 일기 목록 
    path('diary/info/', views.info, name="info"), # 감정 일기에 대한 설명
    # path('diary/write/', views.page_create, name="page-create"), # 새로운 일기 작성
    path('diary/page/<int:post_id>/', views.page_detail, name="page-detail"), # 각각의 일기 내용
    # path('diary/page/<int:post_id>/edit/', views.page_update, name="page-update"), # 각각의 일기 수정
    # path('diary/page/<int:post_id>/delete/', views.page_delete, name="page-delete"), # 각각의 일기 삭제
]
