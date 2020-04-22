from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all().order_by('-published')[:6]
    context = {'posts': posts}
    return render(request, 'main/index.html', context)


def post_create(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    context = {'form': form}
    return render(request, 'main/post_create.html', context)


def post_edit(request, post_id):
    post = Post.objects.filter(id=post_id)[0]
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    context = {'form': form, 'post': post}
    return render(request, 'main/post_edit.html', context)


def about(request):
    return render(request, 'main/about.html')


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context