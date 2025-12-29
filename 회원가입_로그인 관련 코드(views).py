# 강의
from django.conf import settings  # 실행되고 있는 dijango내 conf에서 가져오는것

# from config import settings config의 파일내에 setting를 가져 오는것
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User


def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN.URL)

    return render(request, "registration/signup.html", {"form": form})


# v1
def login(request):
    form = AuthenticationForm(request, request.POST or None)
    django_login(request, form.get_user())
    return redirect("/")
    context = {"form": form}
    return render(request, "registration/login.html", context)


# v2
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            django_login(request, user)
            return redirect(reverse("blog_list"))
    else:
        form = AuthenticationForm(request)

    context = {"form": form}

    return render(request, "registration/login.html", context)


# 실무
def sign_up(request):
    """
    GET  : 회원가입 폼
    POST : 회원 생성 + 자동 로그인
    """

    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()  # 사용자 생성
        django_login(request, user)  # 로그인 처리
        return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "registration/signup.html", {"form": form})


# 실무2
# =========================
# 📝 회원가입
# =========================
def sign_up(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        django_login(request, user)  # 회원가입 후 자동 로그인
        return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "registration/signup.html", {"form": form})


# =========================
# 🔐 로그인
# =========================
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # ⭐ 핵심
            user = form.get_user()
            django_login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = AuthenticationForm(request)

    return render(request, "registration/login.html", {"form": form})
