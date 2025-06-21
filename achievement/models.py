from django.db import models


# Create your models here.


class Category(models.Model):
    # 分类名称
    name = models.CharField(max_length=50, verbose_name='分类名称', unique=True)
    # 描述
    description = models.TextField(blank=True, verbose_name='描述')
    # 创建时间
    created_at = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        db_table = 'category'


class Achievement(models.Model):
    class Meta:
        db_table = 'achievements'

    # 逻辑外键用户名 user.model.UserModel
    username = models.CharField(max_length=100, verbose_name="逻辑外键用户名")
    # 成果名
    name = models.CharField(max_length=100, verbose_name="成果名", default="")
    # 成果类别
    category = models.CharField(max_length=100, default='其他', verbose_name="成果的类型")
    # 成果描述
    description = models.CharField(max_length=100, verbose_name="成果描述")
    # 取得时间
    datetime = models.DateTimeField(null=False, blank=False, verbose_name="获取时间")
    # 文件
    file = models.FileField(upload_to='achievements/', default='achievements/none.png', verbose_name="文件")
    # 是否公开
    is_published = models.BooleanField(default=False, verbose_name="是否公开")

    def __str__(self):
        return self.description
