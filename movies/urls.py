from django.urls import path
from . import views


urlpatterns = [
    path('',views.movie_list,name='movie_list'),
    path('registration/',views.registration, name='registration'),
    path('login/',views.log_in,name='login'),
    path('detail/<int:id>',views.movie_detail,name='detail'),
    path('about/',views.about,name='about'),
    path('category/',views.category,name='Category')
]