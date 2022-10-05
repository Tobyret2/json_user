from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','username','phone','address','slug')
    prepopulated_fields = {'slug':('name','phone')}

