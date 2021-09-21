from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100) # 제목
    content = models.TextField() # 내용
    feeling = models.CharField(max_length=80) # 감정 상태
    score = models.IntegerField() # 감정 점수
    dt_created = models.DateField() # 작성일
    
    def __str__(self):
        return self.title