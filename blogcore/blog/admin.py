from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)
@admin.register(Post) #Навести красоту в админке
class Postadmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status') # список
    list_filter = ('status', 'created', 'publish', 'author')# фильтр справа
    search_fields = ('title', 'body') #Строка поиска
    date_hierarchy = 'publish' #Под поиском добавлены ссылки для навигации по датам
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug': ('title',)}  # Генирирование автоматического slug
    raw_id_fields = ('author',)  # Поиск автора в форме создания статьи
