from django.urls import path     
from . import views

urlpatterns = [
        path('',views.index),
        path('process_money/<str:ubicacion>',views.processMoney),
        path('resetcounter',views.resetCounterGold),	   
]
