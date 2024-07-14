from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
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
def registration(reqeust):
    if reqeust.method =='POST':
        form = forms.SingUpForm(reqeust.POST)
        if form.is_valid():
            user = form.save()
            login(reqeust,user)
            return redirect('homepage')
    else:
        form = forms.SingUpForm()
    return render(reqeust,'registration.html',{'form':form})

def log_in(request):
    if request.method =='POST':
        form = forms.SignInForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('movie_list')
    else:
        form = forms.SignInForm()
    return render(request,'login.html',{'form':form})

def movie_detail(request,id):
    post = get_object_or_404(models.Movies,id=id)
    return render(request,'movie_detail.html',{'post':post})

class SingInClass(LoginView):
    authentication_form = forms.SignInForm
    template_name='login.html'


def movie_detail(request,id):
    movie = get_object_or_404(models.Movies,id=id)
    comments = models.Comments.objects.all()
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.movie = movie
            new_comment.author = request.user
            new_comment.save()
            return redirect('detail',id=movie.id)
    else:
            comment_form = forms.CommentForm()
    return render(request,'movie_detail.html',{
        'movie':movie,
        'comments':comments,
        'comment_form':comment_form
        })


def about(request):
    return render(request, 'about.html')