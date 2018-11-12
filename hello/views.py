from django.shortcuts import render, HttpResponse
from hello.models import User

# Create your views here.

#
# class User:
#     def __init__(self, username, age):
#         self.username = username
#         self.age = age



def index(request):
    # return HttpResponse('hello world')
    # name = 'tom'
    user1 = User(username='马云',
                 age=33)
    # user1.save()
    user2 = User(username='玛丽莲',
                 age=44)
    # user2.save()
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})
