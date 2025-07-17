from django.shortcuts import render
from .forms import MysiteForm,BlogForm
from django.http import HttpResponseRedirect
from .models import BlogPost,TempCart,GamePurchase
from django.http import Http404

# Create your views here.

# All Post 
def All_post(request):
    cards = BlogPost.objects.all()
    return render(request,"blog/allpost.html",{
        'cards':cards
                })

# Latest 3 cards in introduction
def Mysite(request):     
    post = BlogPost.objects.all()
    latest_post = post[::-1][:3]
    return render(request,'blog/introduction.html',{
        'latest_post':latest_post
    })

# Card details
def Carddetails(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404("Post not found")
    return render(request, 'blog/postdetails.html', {
        'post': post,
    })


# Contact Form
def ContactForm(request):
    if request.method == 'POST':
        form = MysiteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        else:
            print("Form errors:", form.errors)
            return render(request, "blog/form.html", {
                'form': form,
            })
    else:
        form = MysiteForm()
    return render(request, "blog/form.html", {
        'form': form
    })


# Blog Form- To add new blog
def Blog_Form(request):
    if request.method == 'POST':
        postform = BlogForm(request.POST,request.FILES)

        if postform.is_valid():
            print("Form is valid")
            print(postform)
            postform.save()
            return HttpResponseRedirect('/blog-thankyou')
        else:
            print("Form is invalid")
            print(postform.errors)
            return render(request,'blog/postform.html',{
                'postform':postform
            })
    
    postform = BlogForm()
    return render(request,"blog/postform.html",{
        'postform' : postform
    })

#To add game in Temporary model
def AddtoCart(request,slug):
    if request.method == 'POST':
        game = BlogPost.objects.get(slug=slug)
        TempCart.objects.create(game=game)
        return HttpResponseRedirect('/usercart')

def CartView(request):
    cart_items = TempCart.objects.all()
    total = 0 
    game_list = []
    for items in cart_items:
        total = total+items.game.price
        game_list.append(items.game.title)

    game_title = ", ".join(game_list)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        GamePurchase.objects.create(name=name,email=email,contact=contact,total=total,games_purchased=game_title)

        TempCart.objects.all().delete()
        return HttpResponseRedirect('/cart-thankyou')
    
    return render(request,'blog/usercart.html',{
        'cart_items' : cart_items,
        'total':total
        
    })

def AdminDashboard(request):
    details = GamePurchase.objects.all()
    return render(request,"blog/admindashboard.html",{
        'details':details
    })

# delete game from cart
def DeleteGame(request,id):
        if request.method == 'POST':
            item = TempCart.objects.filter(id=id)
            if item:
                item.delete()
        return HttpResponseRedirect("/usercart")

# Blog ThankYou page
def Blogthankyou(request):
    return render(request,'blog/postthankyou.html')

# Contact Thankyou page
def ThankYou(request):
    return render(request,'blog/thankyou.html')

#Cart Purchase Thankyou page
def Cartthankyou(request):
    return render(request,'blog/cartthankyou.html')