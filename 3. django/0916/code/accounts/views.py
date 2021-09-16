from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm
from IPython import embed


def index(request):
    accounts = get_user_model().objects.all()
    context = {
        'accounts': accounts,
    }
    return render(request, 'accounts/index.html', context)


# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
    # return render(request, 'accounts/signup.html', context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
            # request.GET -> 주소
            # request.GET.get('next') -> ?=next= /articles/4/update 같은 next를 낀 주소
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
    # return render(request, 'accounts/login.html', context)


def logout(request):
    if not request.user.is_authenticated:
        return redirect('articles:index')
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')


@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
    # return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # embed()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)
    # return render(request, 'accounts/change_password.html', context)