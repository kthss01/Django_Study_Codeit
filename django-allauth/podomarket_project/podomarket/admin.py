from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post

# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname", "kakao_id", "address")}),)

admin.site.register(Post)