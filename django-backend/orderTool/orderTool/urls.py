"""orderTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework import routers
from backend import views
from django.conf.urls import url, include

auth_router = routers.DefaultRouter()
auth_router.register('api/auth/user_manager', views.UserManager, base_name="user_manager")
auth_router.register('api/auth/user_rigister', views.UserRigister, base_name="user_rigister")

models_url = [
    path('', include(auth_router.urls)),
]


admin_url = [
    path('admin/', admin.site.urls),
]

jwt_token_url = [
    path('api/token/obtain/', obtain_jwt_token, name='token_obtain'),
    path('api/token/refresh/', refresh_jwt_token, name='token_refresh'),
    path('api/token/verify/', verify_jwt_token, name='token_verify'),
]

urlpatterns = admin_url + jwt_token_url + models_url