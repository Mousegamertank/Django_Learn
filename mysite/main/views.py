from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index (response):
    return HttpResponse('<h1>Pedro List</h1>' )

#def showId (response, id):
 #   return HttpResponse('<h1>{}</h1>'.format(id))

def showName(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse('<h1>{}</h1>'.format(ls.name))

def showNameDire(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse('<h1>{}</h1><br></br><p>{}</p>'.format(ls.name, str(item.text)))

def v1(response):
    return HttpResponse('<h1> Deus Viniscius comedor de todas </h1>')