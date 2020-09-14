from django.urls import path
from . import views
urlpatterns =[path("get",views.index1,name="index1"),path("",views.index,name = "index"),path("register",views.dindex,name = "dindex")]