from django.shortcuts import render
from django.http import HttpResponse

from .tasks import test_func


def check():
    x=1
    y=2
    return x+y


def say_hello(request):
    # return HttpResponse('Hello world')
    x=check()
    print(x)
    return render(request, 'hello.html', {'name':None})


def test(request):
    test_func.apply_async(queue='CELERY-SILVER-PRIORITY-1')
    return HttpResponse("Done")
