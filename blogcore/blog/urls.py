
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', post_list),

    # path('post/<int:year>/<int:month>/<int:day>/<<slug:post>/',post_detail,name="post_detail_url"),
]
