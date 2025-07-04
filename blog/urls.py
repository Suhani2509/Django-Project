from django.urls import path
from . import views
urlpatterns=[
    path('',views.Mysite),
    path('all-post',views.All_post,name='all-post'),
    path('all-post/<slug:slug>/',views.Carddetails,name='data-visualization'),
    path('contact',views.ContactForm,name='contact'),
    path('postform',views.Blog_Form,name='postform'),
    path('thank-you',views.ThankYou)
]
