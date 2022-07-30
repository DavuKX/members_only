from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
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
        'posts/post_detail.html',
        {'post': post}
    )
@login_required
def new_post(request):
    new_post = False
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.status = 'Published'
            new_post.save()
    else:
        post_form = PostForm()
    
    return render(
        request,
        'posts/new_post.html',
        {'post_form': post_form,
         'new_post': new_post}
    )