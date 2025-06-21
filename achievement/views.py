from django.shortcuts import render, redirect
from django.urls import reverse

from achievement.models import Category, Achievement


# Create your views here.


def add_achievement(request):
    if request.method != 'POST':
        return redirect("control")

    username = request.POST.get('username')
    name = request.POST.get('name')
    datetime = request.POST.get('achieved_date')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    category = request.POST.get('category')
    is_public = request.POST.get('is_public')
    if all([name, datetime, description, category, is_public]):
        created = Achievement.objects.create(
            username=username,
            name=name,
            datetime=datetime,
            description=description,
            category=category,
            is_published=is_public
        )
        if file is not None:
            created.file = file
        created.save()

    return redirect(reverse("control") + "#achievement-section")


def delete_achievement(request):
    if request.method != 'POST':
        return redirect("control")

    _id = request.POST.get('id')
    if _id is not None:
        deleted = Achievement.objects.get(id=_id)
        deleted.file.delete()
        deleted.delete()

    return redirect(reverse("control") + "#achievement-section")


def toggle_publish_achievement(request):
    if request.method != 'POST':
        return redirect("control")

    _id = request.POST.get('id')
    if _id is not None:
        toggled = Achievement.objects.get(id=_id)
        toggled.is_published = not toggled.is_published
        toggled.save()

    return redirect(reverse("control") + "#achievement-section")


def add_category(request):
    if request.method != "POST":
        return redirect("control")

    name = request.POST.get("name")
    description = request.POST.get("description")
    if all([name, description]):
        category = Category(name=name, description=description)
        category.save()

    return redirect(reverse("control") + "#category-section")


def delete_category(request):
    if request.method != "POST":
        return redirect("control")

    id = request.POST.get("id")
    if id is not None:
        category = Category.objects.get(id=id)
        category.delete()

    return redirect(reverse("control") + "#category-section")

