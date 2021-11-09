from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.template import loader


def posts_list(request):
    # html = "<ul>"
    # for post in Post.objects.all():
    #     html += f"<li>{post}</li>"
    # html += "</ul>"
    posts = Post.objects.all()
    # template = loader.get_template('posts/list.html')
    context = {'posts_list': posts}
    return render(request, "posts/list.html", context=context)


def posts_first(request, arg=4):
    html = "<div>"
    one_post = Post.objects.filter(pk=arg)

    # for post in Post.objects.filter(id=1):
    #     html += f"<li>{post}</li>"
    context = {'one_post': one_post[0]}
    return render(request, 'posts/details.html', context)
