
from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo,name='demo'),

    # path('',views.helo,name='helo'),
    #path('add/', views.operation,name='operation')
]

