from django.urls import path
from  . import views

urlpatterns=[path('',views.add_review),
             path('display/',views.display_review),
             ]