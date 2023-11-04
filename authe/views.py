from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserSignUpForm, UserSignInForm
from .models import User


# Create your views here.
class Register(View):
    def get(self, request):
        form = UserSignUpForm()
        context = {
            'form': form
        }
        return render(request, 'authe/index.html', context=context)
    
    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            # User.objects.create(
            #     username=request.POST['username'],
            #     email=request.POST['email'],
            #     first_name=request.POST['first_name'],
            #     last_name=request.POST['last_name'],
            #     password=request.POST['password'],
            # )
            form.save()
            return redirect(reverse_lazy('authe:login'))
        else:
            context = {
                'form': form
            }
            return render(request, 'authe/index.html', context=context)
        

@method_decorator(login_required, name='get')
class Profile(LoginRequiredMixin, View):
    login_url = '/authe/signin/'

    def get(self, request):
        return render(request, 'authe/profile.html')
    

class Login(View):
    def get(self, request):
        form = UserSignInForm()
        context = {
            'form': form
        }

        return render(request, 'authe/signin.html', context=context)
    
    def post(self, request):
        form = UserSignInForm(request, request.POST)

        if form.is_valid():
            try:
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return redirect(reverse_lazy('authe:profile'))
            except:
                return render(request, 'authe/signin.html', context={'form': form, 'err': '1'})
        else:
            return render(request, 'authe/signin.html', context={'form': form, 'err': 2})