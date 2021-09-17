from django.shortcuts import render, redirect
from .models import Community
from .forms import CommunityForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_safe
def index(request):
    communities = Community.objects.all()
    context = {
        'communities': communities,
    }
    return render(request, 'community/index.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save()
            return redirect('community:detail', community.pk)
    else:
        form = CommunityForm()
    context = {
        'form': form
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, pk):
    community = Community.objects.get(pk=pk)
    context = {
        'community': community,
    }
    return render(request, 'community/detail.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    community = Community.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            form.save()
            return redirect('community:detail', community.pk)
    else:
        form = CommunityForm(instance=community)
    context = {
        'community': community,
        'form': form,
    }
    return render(request, 'community/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        community = Community.objects.get(pk=pk)
        community.delete()
    return redirect('community:index')
