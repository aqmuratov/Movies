from django.shortcuts import render,get_list_or_404,redirect

from . import models

# Create your views here.
def movie_list(request,category_slug=None):
    category = None
    categories = models.Category.objects.all()
    movies = models.Movies.objects.all()
    if category_slug:
        category = get_list_or_404(models.Category,slug=category_slug)
    return render(request,'movie_list.html',{
        'category':category,
        'categories':categories,
        'movies':movies,
    })