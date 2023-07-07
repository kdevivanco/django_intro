from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# our view folder is a serves as a request handler
# it is a collection of functions that take a request and return a response
# the request is an object that contains information about the request
# the response is an object that contains information about the response

#our first function 

def  calculate():
    x =10 
    y = 1
    return x

def say_hello(request):
    x = calculate()
    name = 'b'
    # return HttpResponse("Hello World")
    # we can create some variable and send it to a template
    # we can also return a template
    return render(request,'hello.html',{'name':name})


#to run without having to call manage.py 
# at top on menu -> run without debugging
