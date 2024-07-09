from django.shortcuts import render,get_list_or_404,redirect
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
        form = forms.AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('homepage')
    else:
        form = forms.AuthenticationForm()
    return render(request,'login.html',{'form':form})


class SingInClass(LoginView):
    authentication_form = forms.SignInForm
    template_name='registration.html'
