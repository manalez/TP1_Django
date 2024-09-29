from django.urls import path
from .views import register, login_view, welcome_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('welcome/<str:username>/', welcome_view, name='welcome'),
]
