from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name 
    def get_absolute_url(self):
        return reverse('movies:category',args=[self.slug])

class Movies(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название фильма')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    realised_date = models.DateField(verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Описание фильма')
    image = models.ImageField(verbose_name='Обложка фильма')
    trailer = models.URLField(verbose_name='Ссылка для трейлера',blank=True,null=True)

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'

    def __str__(self) -> str:
        return self.name 
    def get_absolute_url(self):
        return reverse('movies:movie',args=[self.id,self.slug])
    
class Comments(models.Model):
    author = models.ForeignKey(User,max_length=300,on_delete=models.CASCADE)
    text = models.TextField(max_length=600,verbose_name='Техт')
    created_date = models.DateField(verbose_name='время писание')
    movie = models.ForeignKey(Movies,verbose_name='Фильм',on_delete=models.CASCADE)
    

