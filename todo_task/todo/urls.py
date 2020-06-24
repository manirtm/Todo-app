from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',  views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/',  views.login, name='login'),
    path('create/', views.create, name='create'),
    path('reopen/<int:id>', views.reopen, name='reopen'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]
