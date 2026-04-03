from django.urls import path
from . import views
urlpatterns=[path('',views.register_course),
             path('display/',views.display_course),]