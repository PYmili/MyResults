from django.shortcuts import render, redirect, reverse

from news.models import News


# Create your views here.


def add_news(request):
    if request.method != 'POST':
        return redirect("control")

    title = request.POST.get('title')
    content = request.POST.get('content')
    if all([title, content]):
        news = News.objects.create(title=title, content=content)
        news.save()

    return redirect(reverse("control") + "#news-section")


def delete_news(request):
    if request.method != 'POST':
        return redirect("control")

    _id = request.POST.get('id')
    if _id is not None:
        news = News.objects.get(id=_id)
        news.delete()

    return redirect(reverse("control") + "#news-section")
