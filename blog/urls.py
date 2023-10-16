from django.urls import path
from blog import views

urlpatterns = [
    path('hello/', views.hello_world, name='blog-hello_world')
]