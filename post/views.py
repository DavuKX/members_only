from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'posts/post_list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(
        request,
        'blog/post/post_detail.html',
        {'post': post}
    )