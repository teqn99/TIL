from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm


User = get_user_model()

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect(request.GET.get('next') or 'community:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('community:index')


def logout(request):
    auth_logout(request)
    return redirect('community:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('community:index') 


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), username=username)
        if person != request.user:  # 팔로우를 누른 사람과 할 사람이 같지 않다면
            if person.followers.filter(pk=request.user.pk).exists():
                # 나의 팔로우 목록에 팔로우를 하려고 하는 사람이 있다면 == 현재 페이지 주인의 팔로워 목록에 내가 있다면
                # 팔로우 목록에서 팔로우하려는 사람을 제거
                person.followers.remove(request.user)
            else:
                # 나의 팔로우 목록에 팔로우를 하려고 하는 사람이 없다면
                # 팔로우 목록에서 팔로우하려는 사람을 추가
                person.followers.add(request.user)
            return redirect('accounts:profile', person.username)
    return redirect('accounts:login')