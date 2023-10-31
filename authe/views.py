from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserSignUpForm
from django.views import View
from django.http import HttpResponse

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
            User.objects.create(
                username=request.POST['username'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                password=request.POST['password1'],
            )
            return redirect(reverse_lazy('products:index'))
        else:
            context = {
                'form': form
            }
            return render(request, 'authe/index.html', context=context)
            return redirect(reverse_lazy('authe:signup'))
        