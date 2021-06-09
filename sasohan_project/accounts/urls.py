from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
	path('signup/', views.signup, name="signup"),
	path('logout/', views.logout, name="logout"),
	
	path('cert-email/<username>/<token>/', views.certEmail, name="certEmail"),
	path('activate-email', views.activateEmail, name="activate-email")
]