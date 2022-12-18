# backend/apps/accounts/urls.py file

from django.conf.urls import url, include
from django.urls import path, re_path

accounts_urlpatterns = [
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
]
