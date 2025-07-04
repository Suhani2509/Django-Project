from django.shortcuts import render
from .forms import MysiteForm,BlogForm
from django.http import HttpResponseRedirect
from .models import BlogPost
from django.http import Http404

# Create your views here.
def All_post(request):
    cards = BlogPost.objects.all()
    return render(request,"blog/allpost.html",{
        'cards':cards
                })


def Mysite(request):
    post = BlogPost.objects.all()
    latest_post = post[::-1][:3]
    return render(request,'blog/introduction.html',{
        'latest_post':latest_post
    })

def Allpost(request):
    return render(request,'blog/allpost.html')

def ContactForm(request):
    if request.method == 'POST':
        form = MysiteForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')

    
    form = MysiteForm()
    return render(request,"blog/form.html",{
        'form' : form
    })

def Blog_Form(request):
    if request.method == 'POST':
        postform = BlogForm(request.POST,request.FILES)

        if postform.is_valid():
            print(postform)
            postform.save()
            return HttpResponseRedirect('/postform',{
                'postform':postform
                
            })
        else:
            print(postform.errors)
    
    postform = BlogForm()
    return render(request,"blog/postform.html",{
        'postform' : postform
    })

def ThankYou(request):
    return render(request,'blog/thankyou.html')

def Carddetails(request,slug):
    try:
        post = BlogPost.objects.get(slug=slug)
    except:
        return Http404
    return render(request,'blog/postdetails.html',{
        "post" : post,
    })