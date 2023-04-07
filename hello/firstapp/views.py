from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски"]
    return render(request, "firstapp/index.html"),
                #   context={"cat": cat})

    # header = "персональные данные"
    # langs = ["Английский", "Немецкий", "Испанский"]
    # user = {"name" : "Максим", "age" : 30 }
    # addr = ("Виноградная", 23, 45)
    # data = {"header" : header, "langs": langs, "user": user, "address": addr}
    #data = {"header": "Передача параметров в шаблон Django",
     #       "message" : "Загружен шаблон hello/templates/firstapp/index_app1.html "}
    # return render (request, "index.html", context=data)


def about(request):
    return HttpResponse("<h2> О сайте </h2>")

def contact(request):
    return HttpResponse("<h2> Контакты </h2>")

def products(request,productid):
    category = request.GET.get("cat", "")
    output = "<h2> Продукт № {0} Категория {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request, id, name):
    id= request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1} </h3>".format(id, name)
    return HttpResponse(output)
