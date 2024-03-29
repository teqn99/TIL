from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm
from IPython import embed
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_safe
def index(request):
    # embed()  # django 디버깅을 위해 화면을 멈추는 것 -> 터미널 창에서 IPython이 켜진 걸 확인할 수 있다.
    if request.session:
        # 로그인 했을 때
        visits_num = request.session.get('visits_num', 0)  # dict 문법, visits_num을 들고 오는 데 없으면 0을 들고 옴.
        request.session['visits_num'] = visits_num + 1
    else:
        # 로그인 안했을 때
        visits_num = 0

    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
        'visits_num': visits_num,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# @login_required  # 로그인 창으로 보내주면서, 다시 delete로 보내는 과정은 GET 방식으로 보냄.
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
