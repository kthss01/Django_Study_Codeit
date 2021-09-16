from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=80) # 음식이름(한글)
    name_eng = models.CharField(max_length=80) # 음식이름(영어)
    description = models.CharField(max_length=120) # 음식설명
    price = models.IntegerField() # 음식가격
    img_path = models.CharField(max_length=255) # 사진 파일 경로
    
    def __str__(self) -> str:
        return self.name
    
    