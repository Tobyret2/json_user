from django.shortcuts import render
from .models import User
import requests

try:
    NUM = len(User.objects.all())
except:
    pass


def add_user(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    jsd = requests.get(url).json()
    global NUM
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
    show_add_button = NUM < len(jsd)

    return render(request, 'user/add_user.html', {'show_add_button': show_add_button})


def about_user(request, user_slug):
    user = User.objects.get(slug=user_slug)

    return render(request, 'user/about_user.html', {'user': user})


def all_users(request):
    all_user = User.objects.all()

    return render(request, 'user/all_user.html', {'all_user': all_user})
