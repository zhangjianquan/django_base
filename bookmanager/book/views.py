from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
'''
所谓的视图，其实就是python函数
视图函数有两个要求：
    1. 视图函数的第一个参数就是接收请求,这个请求其实就是HttpRequest的类对象 （from django.http import HttpReuqest ）
    2. 必须返回一个响应
#我们期望用户输入http://127.0.0.1:8000/index来访问视图函数
'''
def index(request):
    return HttpResponse('ok')