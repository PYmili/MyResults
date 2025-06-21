from django.shortcuts import render, redirect

from achievement.models import Achievement, Category
from common.JwtUtil import JwtUtil
from news.models import News
from user.models import User


# Create your views here.


def control(request):
    jwt = request.COOKIES.get("token")

    if jwt is None or jwt == "":
        return redirect("login")

    verify_jwt = JwtUtil.verify_jwt_token(jwt)
    # jwt验证失败！
    if verify_jwt is None:
        return redirect("login")

    username = verify_jwt.get("username")
    if username is None or username == "":
        return redirect("login")

    user = User.objects.get(username=username)

    sort_by = request.GET.get("sort_by", "datetime")

    achievements = Achievement.objects.order_by(sort_by).filter(username=username)

    category_filter = request.GET.get("category_filter", None)
    if category_filter is not None and category_filter != "":
        achievements = achievements.filter(category=category_filter)

    response = render(request, 'control.html', {
        'user': user,
        'achievements': achievements,
        'categories': Category.objects.all(),
        'users': User.objects.all() if user.is_admin else [],
        'news': News.objects.all()
    })
    return response
