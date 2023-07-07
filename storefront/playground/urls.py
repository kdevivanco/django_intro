from django.urls import path

#here we are going to map our views to our urls (paths)
from . import views
#we will create a url pattern for the home page of our website and call it 'home
#we will map the url pattern to the view function 'say_hello'

# URL CONF
urlpatterns = [
    path('hello/', views.say_hello)
]

# we must import this url to the main project (on the storefront folder)