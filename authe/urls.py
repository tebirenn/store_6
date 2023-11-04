from django.urls import path
from . import views

app_name = 'authe'

urlpatterns = [
    path('signup/', views.Register.as_view(), name='signup'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('signin/', views.Login.as_view(), name='login'),
]