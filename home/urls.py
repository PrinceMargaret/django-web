from django.contrib import admin
from django.urls import path

#from home import views,
from home.views import action 
a=action()
urlpatterns = [
    path("",a.index,name='home'),
    # path("",views.index,name='home'),
    path("about/",a.about,name='about'),
    path("services/",a.services,name='services'),
    path("contact/",a.contact,name='contac')
]