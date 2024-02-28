from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "User login"
admin.site.site_title = "Admin's Portal"
admin.site.index_title = "Welcome to the Ice Cream parlour"

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name='contact')
    
]
