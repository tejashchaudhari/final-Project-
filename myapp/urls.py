from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('property/',views.property),
    path('profile/',views.profile),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('agentsingle/',views.agentsingle),
    path('userlogout',views.userlogout),
    path('agentsgrid/',views.agentsgrid),
    path('blogsingle/',views.blogsingle),
    path('propertysingle/',views.propertysingle),
]
