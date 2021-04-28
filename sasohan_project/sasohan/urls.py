from django.contrib import admin
from django.urls import path, include
from . import views
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name="home"),

    path('login/', views.login, name="login"),
	path('signup/', views.signup, name="signup"),
	path('logout/', views.logout, name="logout"),

    path('accounts/', include('allauth.urls')),	# allAuth (네이버로그인)
]
