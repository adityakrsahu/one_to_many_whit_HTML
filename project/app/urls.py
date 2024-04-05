from django.urls import path
from .views import home,add_dep,add_stu


urlpatterns = [
    path('',home,name='StudentForm'),
    path('add_dep/',add_dep,name='add_dep'),
    path('add_stu/',add_stu,name='add_stu')
]