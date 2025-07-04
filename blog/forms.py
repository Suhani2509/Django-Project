from .models import Gameblog,BlogPost
from django import forms

class MysiteForm(forms.ModelForm):
    class Meta:
        model = Gameblog
        fields = '__all__'
        labels = {
           "name" : "Enter your Name",
           "city" : "Enter your City",
           "email" : "Enter your Email",
           "contact_no" : "Enter your Contact Number"
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'date' : forms.DateInput(attrs={
                'type':"date"
            })
        }
        labels = {
           "title" : "Enter your Title",
           "summary" : "Enter Summary of your blog",
           "date" : "Enter Date",
           "image" : "Upload blog image"
        }