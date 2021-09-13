from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # 날짜 데이터 생성하기
    today = datetime.today().date()
    # print(today) # 개발 서버 콘솔에 출력
    context = {"date" : today}
    return render(request, 'foods/index.html', context=context)
