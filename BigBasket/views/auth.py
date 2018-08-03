from django.views import View
from BigBasket.forms import *
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

class SignUp(View):
    def get(self,request):
        signup = SignupForm
        return render(
            request,
            template_name='registration/signup.html',
            context={'form':signup,'title':'BigBasket|Signup'}
        )

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)

            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('BigBasket:login')

class Login(View):
    def get(self,request):
        login =  LoginForm
        return render(
            request,
            template_name="registration/login.html",
            context={'form':login,'title':'BigBasket|Login'}
        )

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('BigBasket:product_list')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('BigBasket:product_list')


def logout_view(request):
    logout(request)
    return redirect('BigBasket:product_list')


