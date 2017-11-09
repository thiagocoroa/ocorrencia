from django import forms
from .models import Notification, Student

class NotificationForm(forms.ModelForm):
    # TODO: Define other fields here

    def __init__(self,*args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Notification
        fields = ['school','neighborhood','date','period','time',
        'name','involved','involved_description',
        'kind','description_kind','measures','measures_description','contact']


    def clean(self):
        cleaned_data = super(NotificationForm, self).clean()
        return cleaned_data
class StudentForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Student
        fields = ['name','room','age']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        return cleaned_data
