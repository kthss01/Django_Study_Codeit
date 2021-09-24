from .models import Page
import random

def validate_pages():
    pages = Page.objects.all()
    
    for page in pages:
        if page.score < 0 or page.score > 10:
            print(page.id, '번 글의 감정점수 0 ~ 10 사이 아님')
            page.score = random.randint(0, 10) # 0 ~ 10 값 랜덤
            page.save()