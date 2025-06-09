from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:
        db_table = 'users'
    # 用户名
    username = models.CharField(max_length=100)
    # 密码 （hash)
    password = models.CharField(max_length=255)
    # 头像
    avatar = models.ImageField(upload_to='avatars')
    # 是否为公开用户
    is_public = models.BooleanField(default=False)
    # 是否是管理员
    is_admin = models.BooleanField(default=False)
