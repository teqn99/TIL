import re
from django.shortcuts import render
from django.views.decorators.http import require_safe, require_GET
from django.shortcuts import get_object_or_404
from .models import Movie
from .sample import func, df_new
import pandas as pd


@require_GET
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    return render(request, 'movies/recommended.html')


def result(request):
    keyword = request.GET.get('keyword')
    recommend = func(df_new, keyword)
    # html = recommend.to_html()
    # recommend.to_html('./movies/templates/movies/sample.html')
    context = {
        'recommend': recommend,
        'keyword': keyword,
        # 'html': html,
    }
    return render(request, 'movies/result.html', context)
    