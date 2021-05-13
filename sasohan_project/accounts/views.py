from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()

# 로그인 페이지
def login(request):
	if request.method == 'POST':
		# 회원정보 찾기
		user = auth.authenticate(
			request, username = request.POST['username'], password = request.POST['password']
		)

		if user is not None:
			auth.login(request, user)	# Login
			return redirect('home')
		else:
			return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 틀립니다.'})
	else:
		return render(request, 'login.html')

# 회원가입 페이지
def signup(request):
	# POST방식으로 요청되면 (회원가입 요청)
	if request.method == 'POST':
		# 아이디 또는 비밀번호가 빈칸일 경우
		if request.POST['username'] == "" or request.POST['password1'] == "":
			return render(request, 'signup.html', {'error': '아이디와 비밀번호를 입력해주세요.'})

		# 전화번호가 빈칸일 경우
		if request.POST['phone'] == "":
			return render(request, 'signup.html', {'error': '핸드폰번호를 입력해주세요.'})

		# 비밀번호 두개가 다를 경우
		if request.POST['password1'] != request.POST['password2']:
			return render(request, 'signup.html', {'error': '비밀번호가 다릅니다.'})
		
		# 회원정보 추가
		user = User.objects.create_user(
			username=request.POST['username'],
			password=request.POST['password1'],
			phone=request.POST['phone']
		)
		# 로그인 처리
		auth.login(request, user)
		# blog 페이지로 redirect
		return redirect('home')
	else:
		return render(request, 'signup.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
	return render(request, 'login.html')