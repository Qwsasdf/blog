
from django.shortcuts import render , get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    posts_draft=Post.objects.all().filter(status="draft")
    return render(request,"blog/post/post_list.html",context={"posts":posts,"posts_draft":posts_draft})

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status="published",publish__year=year,
                             publish__month=month,publish__day=day)
    render(request,"blog/post/post_detail.html",{"post":post})




