from django.contrib import admin
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):#type: ignore
	list_display = ('id', 'username', 'email', 'date_joined')

admin.site.register(UserModel, UserModelAdmin) #type: ignore
