from django.db import models
from .validators import validate_no_hash, validate_no_numbers, validate_score

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, validators=[validate_no_hash]) # 제목
    content = models.TextField(validators=[validate_no_hash]) # 내용
    feeling = models.CharField(max_length=80, validators=[validate_no_hash, validate_no_numbers]) # 감정 상태
    score = models.IntegerField(validators=[validate_score]) # 감정 점수
    dt_created = models.DateField() # 작성일
    
    def __str__(self):
        return self.title