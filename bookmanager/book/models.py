from django.db import models

# Create your models here.
'''
1. 我们的模型类，需要继承子models.Model
2. 系统会自动为我们添加一个主键 --id
3. 字段
        字段名=model.类型(选项)
        字段名就是数据表的字段名，字段名不要使用python,mysql的关键字
'''

class BookInfo(models.Model):
    name=models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BoolenField()
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
