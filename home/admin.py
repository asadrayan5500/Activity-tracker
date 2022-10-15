from django.contrib import admin
from home.models import ActivityList
from home.models import Index , logins
# Register your models here.

admin.site.register(ActivityList)
admin.site.register(Index)

class loginsAdmin( admin.ModelAdmin ):
    list_display = ( 'username' , 'password')

admin.site.register(logins , loginsAdmin)