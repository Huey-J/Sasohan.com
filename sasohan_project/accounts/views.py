from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage	# 이메일 라이브러리
from django.conf import settings
import re		# 정규표현식
import hashlib 	# 해시 암호화

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
		input_username, input_password1, input_password2, input_phone = request.POST['username'], request.POST['password1'], request.POST['password2'], request.POST['phone']
		email_validator = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

		# 아이디 또는 비밀번호가 빈칸일 경우
		if input_username == "" or input_password1 == "":
			return render(request, 'signup.html', {
				'input_username': input_username,
				'input_phone': input_phone,
				'error': '아이디와 비밀번호를 입력해주세요.'
			})

		# 이메일 형식 검사
		if email_validator.match(input_username) == None:
			return render(request, 'signup.html', {
				'input_username': input_username,
				'input_phone': input_phone,
				'error': '잘못된 이메일 형식입니다.'
			})

		# 전화번호가 빈칸, 문자포함, 10자 이하면 에러
		if input_phone == "" or str(input_phone).isdigit() == False or len(input_phone)<10:
			return render(request, 'signup.html', {
				'input_username': input_username,
				'input_phone': input_phone,
				'error': '핸드폰번호를 입력해주세요.'
			})
		
		# 비밀번호 두개가 다를 경우
		if input_password1 != input_password2:
			return render(request, 'signup.html', {
				'input_username': input_username,
				'input_phone': input_phone,
				'error': '비밀번호가 다릅니다.'
			})
		
		# 비밀번호 형식 검사 (8자 이상 20자 이하의 숫자, 영문 조합)
		if len(input_password1) >= 8 and len(input_password1) <= 20 and re.findall('[0-9]+', input_password1) and re.findall('[a-zA-Z]+', input_password1) and not re.findall('[^0-9a-zA-Z]', input_password1):
			try:
				tmp_token = hashlib.md5((input_username + input_password1 + input_phone).encode()).hexdigest()
				tmp_link = settings.DOMAIN + "/accounts/cert-email/" + input_username + "/" + tmp_token
				user = User.objects.create_user(	# 회원정보 추가
					username = input_username,
					password = input_password1,
					phone = input_phone,
					nickname = tmp_token
				)
				# 이메일 보내기
				email_body = """\
    				<html>
      					<head></head>
      					<body>
        					<table width="580" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
							<tbody><tr><td height="40"></td></tr><tr><td>
										<table width="580" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="margin:0 auto;">
										<tbody><tr><td height="3" width="40" bgcolor="#1ea1f7"></td><td height="3" width="500" bgcolor="#1ea1f7"></td><td height="3" width="40" bgcolor="#1ea1f7"></td></tr><tr><td></td><td>
													<table width="500" border="0" cellpadding="0" cellspacing="0">
													<tbody><tr><td height="64"></td></tr><tr><td align="center" height="32">
															<h1>SASOHAN.COM</h1>
															</td></tr><tr><td height="24">
															</td></tr></tbody>
													</table>
												</td><td></td></tr><!-- E: HEADER --><!-- S: BODY --><tr><td></td><td>
								<table width="500" border="0" cellpadding="0" cellspacing="0">
									<tbody><tr><td height="32" style="font-size:24px;text-align: center">
										회원가입 이메일 인증 안내
										</td></tr><tr><td height="40"></td></tr><tr><td height="40" style="line-height: 1.5;font-size: 16px; word-break: keep-all;">
										<strong style="font-weight: bold">안녕하세요,</strong><br>
										회원님의 이메일 %s로 사소한닷컴의 계정이 생성되었으며
										<br>메일 인증을 위해 아래 링크(URL)을 클릭하시면 회원가입이 완료됩니다.
										</td></tr><tr><td height="40"></td></tr><tr><td height="21" style="font-size: 18px;">
										인증 링크
										</td></tr><tr><td height="8"></td></tr><tr><td bgcolor="#f3f5f7" style="padding: 16px;word-break: line-height: 1.43;font-size:14px;">
										<a href="%s" rel="noreferrer noopener" target="_blank">%s</a>
										</td></tr>
									</td></tr></tbody>
								</table>
							</td><td></td></tr><!-- E: BODY --></tbody>
							</table>
							</td></tr><tr><td height="40"></td></tr></tbody>
							</table>
      					</body>
    				</html>
    				""" % (input_username, tmp_link, tmp_link)
				tmp_email = EmailMessage('[사소한닷컴] 회원가입 이메일 인증 안내', email_body, to=[input_username])
				tmp_email.content_subtype = "html"
				tmp_email.send()
				
				auth.login(request, user)	# 로그인 처리
				return redirect('home')		# blog 페이지로 redirect
			except Exception as e:
				print(e)
				return render(request, 'signup.html', {
					'input_username': input_username,
					'input_phone': input_phone,
					'error': '가입된 이메일 입니다: ' + input_username
				})

		else :
			return render(request, 'signup.html', {
				'input_username': input_username,
				'input_phone': input_phone,
				'error': '잘못된 비밀번호 형식입니다. (8자 이상 20자 이하의 숫자, 영문 조합)'
			})
	else:
		return render(request, 'signup.html')

# 로그아웃 함수
def logout(request):
	# if request.method == 'POST':
	# 	auth.logout(request)
	# 	return redirect('home')
	# return render(request, 'login.html')
	auth.logout(request)
	return redirect('home')

# 이메일 인증 페이지
def certEmail(request, username, token):
	print("이메일: " + username)
	print("토큰(닉네임): " + token)
	
	####### 구현필요 #######
	# username, nickname 비교해서 맞으면
	if True:
		return render(request, 'certEmail.html')
	else:
		return 404	# 오류페이지
	

# 이메일 인증
def activateEmail(request):
	if request.method == 'POST':
		input_nickname = request.POST['nickname']
		print(input_nickname)
	else:
		pass
	####### 구현필요 #######
	# nickname, is_cert_email 변경