from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

from common import responses
from common.password import PasswordUtil
from common.JwtUtil import JwtUtil
from user.models import User


# Create your views here.


def handle_login(username: str, password: str) -> responses:
    """
    处理登录
    :param username: 用户名
    :param password: 密码
    :return: common.responses
    """
    if not all([username, password]):
        return responses.RESPONSE_INVALID_PARAMETER

    try:
        user = User.objects.get(username=username)
        if PasswordUtil.check_password(user.password, password) is False:
            invalid = responses.RESPONSE_INVALID_PARAMETER
            invalid['msg'] = '用户或密码错误！'
            return invalid
    except User.DoesNotExist:
        invalid = responses.RESPONSE_INVALID_PARAMETER
        invalid['msg'] = "用户不存在！"
        return invalid

    success = responses.RESPONSE_SUCCESS
    success['msg'] = '登录成功！'
    return success


def handle_register(username: str, password: str) -> responses:
    """
    处理用户注册
    :param username: 需要注册的用户名
    :param password: 需要注册的用户名密码
    :return: common.responses
    """
    if not all([username, password]):
        return responses.RESPONSE_INVALID_PARAMETER

    user_exists = User.objects.filter(username=username).exists()
    if user_exists:
        invalid = responses.RESPONSE_INVALID_PARAMETER
        invalid['msg'] = '用户已存在！'
        return invalid

    try:
        created = User.objects.create(username=username, password=PasswordUtil.password_hash(password))
        created.save()
    except IntegrityError:
        internal = responses.RESPONSE_INTERNAL_ERROR
        internal['msg'] = '服务器错误！'
        return internal

    success = responses.RESPONSE_SUCCESS
    success['msg'] = '注册成功！'
    return success


def login(request):
    if request.COOKIES.get("token") is not None:
        return redirect("control")

    response = None
    jwt = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        action = request.POST.get('action')
        if action is None:
            response = responses.RESPONSE_INVALID_PARAMETER
        elif action == 'login':
            response = handle_login(username, password)
        elif action == 'register':
            response = handle_register(username, password)

        jwt = JwtUtil.generate_jwt_token({
            'username': username,
        })
    if response is not None and response.get('code') == 200:
        _redirect = redirect('control')
        _redirect.set_cookie('token', jwt)
        return _redirect

    return render(request, 'login.html', {
        'response': response
    })


def sign_out(request):
    if request.method != 'POST':
        return redirect('login')

    _id = request.POST.get('id')
    if _id is None:
        return redirect('login')

    try:
        User.objects.get(id=_id)
        response = redirect('home')
        response.delete_cookie("token")
        return response
    except User.DoesNotExist:
        return redirect('login')


def add_user(request):
    if request.method != 'POST':
        return redirect('control')

    username = request.POST.get('username')
    password = request.POST.get('password')
    avatar = request.FILES.get('avatar')
    is_published = request.POST.get('is_published')
    is_admin = request.POST.get('is_admin')
    if all([username, password, avatar]):
        created = User.objects.create(
           username=username,
           password=PasswordUtil.password_hash(password),
           avatar=avatar
        )
        if is_published is not None:
            created.is_published = is_published
        if is_admin is not None:
            created.is_admin = is_admin
        created.save()

    return redirect(reverse('control') + "#user-section")


def delete_user(request):
    if request.method != 'POST':
        return redirect('control')

    _id = request.POST.get('id')
    if _id is not None:
        user = User.objects.get(id=_id)
        user.avatar.delete()
        user.delete()

    return redirect(reverse('control') + "#user-section")


def toggle_publish_user(request):
    if request.method != 'POST':
        return redirect('control')
    _id = request.POST.get('id')
    if _id is not None:
        user = User.objects.get(id=_id)
        user.is_published = not user.is_published
        user.save()

    return redirect(reverse('control') + "#user-section")


def toggle_admin_user(request):
    if request.method != 'POST':
        return redirect('control')

    _id = request.POST.get('id')
    if _id is not None:
        user = User.objects.get(id=_id)
        user.is_admin = not user.is_admin
        user.save()

    return redirect(reverse('control') + "#user-section")