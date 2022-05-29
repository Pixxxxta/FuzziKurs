from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('fazi', views.fazi),
    path('agregator', views.agregator),
    path('defazi', views.defazi),
    path('interface', views.interface),
    path('test', views.btn1),
    path('baza', views.baza),
    path('prinad', views.prinad),
    path('input', views.input),

]
