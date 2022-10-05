from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class User(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя')
    username = models.CharField(max_length=100,verbose_name='Имя пользователя')
    phone = models.CharField(max_length=100,verbose_name='Телефон')
    address = models.CharField(max_length=200,verbose_name='Адрес')
    slug = models.SlugField(unique=True,verbose_name='Slug')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(f'{self.username}-{self.name}')
        super(User,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('about_user' , kwargs= {'user_slug':self.slug})