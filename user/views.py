from django.shortcuts import render
from random import randint
from .models import User
import requests

NUM = len(User.objects.all())


def add_user(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    jsd = requests.get(url).json()
    global NUM
    print(NUM)
    if request.method == 'POST':

        if request.POST.getlist('add') and NUM < len(jsd):
            User.objects.create(
                name=jsd[NUM]['name'],
                username=jsd[NUM]['username'],
                address=jsd[NUM]['address']['city'],
                phone=jsd[NUM]['phone']
            )
            NUM += 1
        elif request.POST.getlist('reset'):
            User.objects.all().delete()
            NUM = 0
    all_user = User.objects.all()

    return render(request, 'user/add_user.html', {'all_user': all_user})


def about_user(request, user_slug):
    user = User.objects.get(slug=user_slug)

    return render(request, 'user/about_user.html', {'user': user})
