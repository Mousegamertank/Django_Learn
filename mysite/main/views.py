from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index (response, id):
    ls = ToDoList.objects.get(id = id)

   #{'save' : ['save'], 'c1': ['clicked']}
    if response.method == 'POST':
        print(response.POST)
        if response.POST.get('save'):
            for item in ls.item_set.all():
                if response.POST.get('c' + str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False

                item.save()
    
        elif response.POST.get('newItem'):
            txt = response.POST.get('new')

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print('inválid')

    return render(response, 'main/list.html', {'ls': ls})

def v1(response):
    return HttpResponse('<h1> Deus Viniscius comedor de todas </h1>')

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            response.user.ToDoList_set.create(name=n)

        return HttpResponseRedirect("/{}".format(t.id))
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})

def view(response):
    return render(response, 'main/view.html', {})

#def showId (response, id):
 #   return HttpResponse('<h1>{}</h1>'.format(id))
'''
def showName(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse('<h1>{}</h1>'.format(ls.name))

def showNameDire(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return HttpResponse('<h1>{}</h1><br></br><p>{}</p>'.format(ls.name, str(item.text)))
'''