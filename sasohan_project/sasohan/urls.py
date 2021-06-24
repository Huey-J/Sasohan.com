from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls'))
]
