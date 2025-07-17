from django.urls import path
from . import views
urlpatterns=[
    path('',views.Mysite,name='home'),
    path('all-post',views.All_post,name='all-post'),
    path('all-post/<slug:slug>/',views.Carddetails,name='data-visualization'),
    path('contact',views.ContactForm,name='contact'),
    path('postform',views.Blog_Form,name='postform'),
    path('add/<slug:slug>',views.AddtoCart,name='addtocart'),
    path('usercart',views.CartView,name='usercart'),
    path("remove-game/<int:id>",views.DeleteGame,name='remove-game'),
    path("admin-dashboard",views.AdminDashboard,name='admin-dashboard'),
    path('thank-you',views.ThankYou),
    path('blog-thankyou',views.Blogthankyou),
    path('cart-thankyou',views.Cartthankyou)
]
