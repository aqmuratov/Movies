from django.urls import path
from . import views


urlpatterns = [
    path('',views.movie_list,name='movie_list'),
    path('registration/',views.registration, name='registration'),
    path('login/',views.log_in,name='login'),
    path('detail/<int:id>',views.post_detail,name='detail'),
]