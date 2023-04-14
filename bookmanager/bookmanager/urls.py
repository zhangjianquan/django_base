"""bookmanager URL Configuration

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
from book.views import index
from django.urls import include

#改成book include以后，访问我们的index需要添加工程的path路由+子应用的path
#127.0.0.1:8000/book/index
#如果不想要/book 可以将下面的配置改成如下配置
urlpatterns = [
    path('admin/', admin.site.urls),
    #path(路由，视图函数名)
    #path('book/',include('book.urls')),
    path('',include('book.urls')),
]
