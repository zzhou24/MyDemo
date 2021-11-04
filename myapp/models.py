from django.db import models
from datetime import datetime

# Create your models here.
# 继承Molde类的增删改查
class Users(models.Model):
    '''自定义User表对应的Model类'''
    # 定义属性：默认逐渐自增id字段可不写
    # id = models.AutoField('ID',primary_key = True)
    name = models.CharField(max_length = 32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length = 16)
    addtime = models.DateTimeField(default=datetime.now)

    # 缩进  如果不指定，则默认自动生成一个由应用名称（即startapp 时使用的名称）加下划线和类名组成的名字对应一个数据库表
    # class Meta:
    #     db_table = 'myapp_users'  #指定表名