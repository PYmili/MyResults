from django.shortcuts import render

from achievement.models import Achievement
from news.models import News
from user.models import User


# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'database_users': User.objects.filter(is_published=True)[:4],
        'achievements': Achievement.objects.filter(is_published=True)[:3],
        'news': News.objects.order_by('datetime').all()[:5],
    })
