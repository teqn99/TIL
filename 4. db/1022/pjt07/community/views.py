from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user.is_authenticated:
        if request.user == review.user: 
            review.delete()
            return redirect('community:index')
    return redirect('community:detail', review.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('community:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('community:index')
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'community/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
        return redirect('community:detail', review.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:detail', review_pk)


@require_POST
def likes(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        # 좋아요를 누른 적이 있다면
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        # 좋아요를 누른 적이 없다면
        else:
            review.like_users.add(request.user)
        return redirect('community:index')
    return redirect('accounts:login')