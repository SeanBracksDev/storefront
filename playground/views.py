from django.shortcuts import render


# Create your views here.
# request -> response
def say_hello(request):
    x = 1
    y = 2
    return render(request, "hello.html", {"name": "Mosh"})
