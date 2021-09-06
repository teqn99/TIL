from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from articles.forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# decorator가 없다면, else문에서 GET이 아닌 다른 동작들이 수행이 가능해지는데,
# decorator를 통해 create라는 함수에는 GET, POST에만 동작하도록 만들어 줌.
@require_http_methods(['GET', 'POST'])
def create(request):
    # create
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
    # new
        form = ArticleForm()
    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')
    

def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    # update
    if request.method == "POST":  # 수정 로직 동작
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # edit
    else:  # GET의 경우 수정 페이지 렌더링
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

