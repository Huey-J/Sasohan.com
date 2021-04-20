from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
	path('signup/', views.signup, name="signup"),
	path('logout/', views.logout, name="logout"),

	path('naver/', include('allauth.urls')),	# allAuth (네이버로그인)
]