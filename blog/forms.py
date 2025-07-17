from .models import Gameblog,BlogPost
from django import forms

class MysiteForm(forms.ModelForm):
    class Meta:
        model = Gameblog
        fields = ['name','city','email','contact_no']
        labels = {
           "name" : "Enter your Name",
           "city" : "Enter your City",
           "email" : "Enter your Email",
           "contact_no" : "Enter your Contact Number"
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.strip())<=2 :
            raise forms.ValidationError("*Name must be more than 2 character")
        return name
    
    def clean_contact_no(self):
        contact_no = self.cleaned_data["contact_no"]
        if len(contact_no.strip())!= 10 or not contact_no.isdigit():
            raise forms.ValidationError('*Please Enter valid 10 digit number')      
        return contact_no
    

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
    
    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title.strip())<=2:
            raise forms.ValidationError("Title must be more than 2 character")
        return title
    
    
    def clean_field(self):
        data = self.cleaned_data["field"]
        
        return data
    