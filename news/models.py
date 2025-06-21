from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datetime = models.DateField(auto_now=True)

    class Meta:
        db_table = 'news'
