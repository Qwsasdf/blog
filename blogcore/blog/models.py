from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
            # Наследуем от Manager класс а его ф-цию get_queryset дополняем через super()
            # фильтр
class Post(models.Model):
    objects = models.Manager()  # Менеджер по умолчанию.
    published = PublishedManager()  # Наш новый менеджер.
    # После добавления менеджера строки 5,6,7,10,11
    # Запросы ниже будут выдавать один и тот же результат
    # Post.published.all()
    # Post.objects.all().filter(status="published")

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
     )
    title = models.CharField(max_length=250)    #Заголовок статьи VARCHAR в БД
    slug= models.SlugField(max_length=250, unique_for_date='publish') #только буквы цифры подчерк
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts") # Внещний ключ к юзеру
                                                           # 1 юзер много статей
                                                            # related_name обратная связь чтоб без _set обращаться
                                                            # Через post = Poet.objects.get(id=1)
                                                            #       post.author.username вместо
                                                            #       post.author__username
    body =models.TextField()
    publish = models.DateTimeField(default=timezone.now) # Тоже что datetime.now только с учетом timezone
    created = models.DateTimeField(auto_now_add=True) # Дата добавляется и сохраняется автоматически при создании
    updated = models.DateTimeField(auto_now=True) # Значение будет автоматически установлено в текущую дату при каждом сохранении
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft') # choices это выбор из кортежа

    # STATUS_CHOICE который выше

    # Методы через shell create(),get(),all(),exclude(),order_by('-title'),delete()
    # Post.objects.filter(publish__year=2017, author__username='admin')[:3] со срезом
    # Post.objects.filter(publish__year=2017).exclude(title__startswith='Why') Исключая те статьи кот нач с WHY

    def get_absolute_url(self):
        return  reverse('blog:post_detail', args=[self.publish.year,
        self.publish.month, self.publish.day, self.slug])

    class Meta:
       ordering=('-publish',) #В запросах порядок будес с последней статьи
    def __str__(self):
        return self.title