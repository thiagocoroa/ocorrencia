from django.contrib import admin
from .models import Notification, Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    """docstring for StudentAdmin."""
    list_display = ['name', 'room', 'age']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['school','neighborhood','date','period','time','involved','involved_description',
    'kind','description_kind','measures','measures_description','contact']
    search_fields = ['school','date','student','kind']
    list_filter =[]

admin.site.register(Notification, NotificationAdmin)
admin.site.register(Student,StudentAdmin)
