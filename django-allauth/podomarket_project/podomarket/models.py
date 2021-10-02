from django.db import models
from django.contrib.auth.models import AbstractUser
from podomarket.validators import validate_no_special_characters

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'}
    ) # 닉네임
    kakao_id = models.CharField(
        max_length=20, 
        null=True,
        validators=[validate_no_special_characters]
    ) # 카카오 ID
    address = models.CharField(
        max_length=40, 
        null=True,
        validators=[validate_no_special_characters]
    ) # 주소
    
    def __str__(self):
        return self.email