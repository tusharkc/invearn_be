import imp
from django.contrib import admin
from django.urls import path
from core_app.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]
