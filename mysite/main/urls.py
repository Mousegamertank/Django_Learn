from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.showName, name='index'),
    path('<str:name>', views.showNameDire, name='index'),
    path('v1/', views.v1, name='index'),
   # path('<int:id>', views.showId, name='index'),
]



