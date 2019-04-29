from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

def hello(request, a):
    print(request.POST.get('key'))
    user_list = User.objects.all()
    return render(request, 'hello/table.html', {'user_list':user_list})

def test(request, id, key):
    print(isinstance(request, HttpRequest))
    print(key)
    return render(request, 'hello/table.html')
# Create your views here.
