from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('v1/', views.v1, name='index'),
    path('', views.home, name='home'),
    path('create/', views.create, name="create")
]
   # path('<int:id>', views.showId, name='index'),
   # path('<int:id>/', views.showName, name='index'),
   # path('<str:name>/', views.showNameDire, name='index'),



