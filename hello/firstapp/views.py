from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "firstapp/home.html")
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
    output = "<h2> Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = "<h2>Пользователь</h2><h3>id:{0} Имя: {1} </h3>".format(id,name)
    return HttpResponse(output)
