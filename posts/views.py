from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from posts.models import Post
from .forms import PostForm


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/add.html', {"form": form})


def add_post(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("posts:add"))
    else:
        form = PostForm()
    return render(request, 'posts/add.html', {'form': form})


def posts_list(request):
    posts = Post.objects.filter(published=True)
    q = request.GET.get("qr")
    if q:
        posts = posts.filter(title__icontains=q)

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)
    context = {'posts_list': posts_list}
    return render(request, "posts/list.html", context=context)


def posts_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {}
    if post.published:
        context['post'] = post
    return render(request, 'posts/details.html', context)
