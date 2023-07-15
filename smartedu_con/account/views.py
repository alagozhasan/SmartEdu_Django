from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
""".user_login,name="login"
ews.user_register,name="
iews.user_dashboard,name
s.user_logout,name="logo"""


def user_login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():  # form geçerli mi
            username = form.cleaned_data["username"]  # bilgileri al
            password = form.cleaned_data["password"]
            user = authenticate(
                req, username=username, password=password
            )  # bilgileri doğruları

            if user is not None:  # kullanıcı var mı
                if user.is_active():  # kullanıcı aktif mi
                    login(req, user)  # login ol
                    return redirect("index")  # indexe geç
                else:
                    # Kullanıcı hesabını etkinleştirmesi gerekiyor!
                    messages.error(req, "Hesabınız pasif.")
            else:
                # bilgielerin geçersiz olduğu durum
                messages.warning(req, "Kullanıcı adı veya şifre yanlış")

    else:
        form = LoginForm()

    return render(req, "login.html", {"form": form})


def user_register(req):
    return render(req, "register.html")


def user_dashboard(req):
    pass


def user_logout(req):
    pass
