from django.urls import path
from . import views

urlpatterns=[path('',views.home),
             path('about/',views.about),
             path('courses/',views.courses),
             path('contact/',views.contact),
             ]
