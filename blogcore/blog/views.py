from django.shortcuts import render, get_object_or_404 
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post 

def catchpage(request):
    return render(request,'blog/post/catch.html')

# def post_list1(request):
#     print()
#     print()
#     print(request.GET)
#     print()
#     print()
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3) # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                    'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


class PostListView(ListView):   #Достаточно этого класса чотбы не писать функцию постраничного вывода
                                # Которая закоментирована выше эту функцию заменяет класс наследник
                                # ListView
                                # с параметром paginate_by = 3
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/post/list.html'

    def get(self, request, *args, **kwargs):
        print(request.GET)
        if request.GET.get("page")=="3":
            PostListView.template_name='blog/post/catch.html'
        return super().get(self,request, *args, **kwargs)