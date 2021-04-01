from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
	if request.method == 'POST':
		# 회원정보 찾기
		user = auth.authenticate(
			request, username = request.POST['account'], password = request.POST['password']
		)

		if user is not None:
			auth.login(request, user)	# Login
			return redirect('home')
		else:
			return render(request, 'login.html', {'error': 'incorrect'})
	else:
		return render(request, 'login.html')

def signup(request):
	if request.method == 'POST':    # POST방식으로 요청되면
		if request.POST['password1'] == request.POST['password2']:  # 입력된 pw 2개 같은지 확인
			# 회원정보 추가
			user = User.objects.create_user(
				username=request.POST['username'],
				password=request.POST['password1']
			)
			# 로그인 처리
			auth.login(request, user)
			# blog 페이지로 redirect
			return redirect('home')
	return render(request, 'signup.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
	return render(request, 'login.html')