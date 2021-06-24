from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 권한 관리 데코레이터

URL_LOGIN = '/accounts/login/'

# 메인 페이지
@login_required(login_url=URL_LOGIN)
def main(request):
    print("어나니머스 트라이 투 엑세스 더 블로그 페이쥐")
    return render(request, 'main.html')