"""w_hub_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import UserView, EmpView
from request.views import Form1View

from rest_framework import routers

route = routers.DefaultRouter()
route.register('', UserView, basename='UserView')

route2 = routers.DefaultRouter()
route2.register('', EmpView, basename='EmpView')

route3 = routers.DefaultRouter()
route3.register('', Form1View, basename='Form1View')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(route.urls)),
    path('emp3/', include(route2.urls)),
    path('form/', include(route3.urls)),

    path('user/', include('user.urls.user_urls')),
    path('emp/', include('user.urls.emp_urls')),
    path('req/', include('request.urls.form_urls')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
