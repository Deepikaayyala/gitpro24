from django.urls import path
from . import views
urlpatterns=[path('',views.add_student),
             path('display/',views.display_student)]