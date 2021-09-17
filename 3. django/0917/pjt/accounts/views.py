from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
# Create your views here.

# 회원가입
@require_http_methods(["GET", "POST"])
def signup(request):
    # 이미 인증되어있는 사용자 검증 후 맞으면 리뷰 페이지로 보내버리기
    if request.user.is_authenticated:
        return redirect('community:index')

    #POST 방식으로 넘어와서 회원가입진행 GET요청이면 빈폼 보내줌
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(["GET", "POST"])
def login(request):
    #인증된 사용자 돌려보내기
    if request.user.is_authenticated:
        return redirect('community:index')
    # 회원 가입진행
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index') #이전 페이지로 갈수 잇도록
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

# GET 방식으로 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('community:index')
