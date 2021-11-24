from django.shortcuts import render
from posts.models import Post


# from django.http import HttpResponse
# from django.template import loader
# html = "<ul>"
# for post in Post.objects.all():
#     html += f"<li>{post}</li>"
# html += "</ul>"
# template = loader.get_template('posts/list.html')


def posts_list(request):
    posts = Post.objects.filter(published=True)
    q = request.GET.get("qr")
    if q:
        posts = posts.filter(title__icontains=q)
    context = {'posts_list': posts}
    return render(request, "posts/list.html", context=context)


def posts_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {}
    if post.published:
        context['post'] = post
    return render(request, 'posts/details.html', context)
