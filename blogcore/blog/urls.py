from django.urls import path
from . import views 


app_name = 'blog'
urlpatterns = [

    # path('req', views.post_list1, name='post_list1'),
    # path('catchpage',views.catchpage, name='catch'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
] 
