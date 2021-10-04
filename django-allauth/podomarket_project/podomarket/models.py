from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
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
    
class Post(models.Model):
    title = models.CharField(max_length=60) # 제목
    item_price = models.IntegerField(validators=[MinValueValidator(1)]) # 물품 가격
    
    CONDITION_CHOICES = [
        ('새제품', '새제품'),
        ('최상', '최상'),
        ('상', '상'),
        ('중', '중'),
        ('하', '하'),
    ]
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default=None) # 물품 상태
    
    item_details = models.TextField(blank=True) # 물품 상세 설명
    
    image1 = models.ImageField(upload_to="item_pics") # 물품 사진
    image2 = models.ImageField(upload_to="item_pics", blank=True) # 물품 사진
    image3 = models.ImageField(upload_to="item_pics", blank=True) # 물품 사진
    
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 게시글 작성자
    
    dt_created = models.DateTimeField(auto_now_add=True) # 게시글 생성 날짜+시간
    dt_updated = models.DateTimeField(auto_now=True) # 게시글 마지막 수정 날짜+시간
    
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title