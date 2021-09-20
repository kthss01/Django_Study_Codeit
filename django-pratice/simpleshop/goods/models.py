from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80) # 상품이름
    price = models.IntegerField() # 상품가격
    img_path = models.CharField(max_length=255) # 이미지경로

    def __str__(self):
        return self.name
