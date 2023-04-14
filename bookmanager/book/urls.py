from django.urls import path
from django.contrib import admin
from book.views import index

urlpatterns = [
    path('index/',index)
]