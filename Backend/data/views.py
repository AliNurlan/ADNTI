from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseBadRequest,HttpResponseForbidden,JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response
 
# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Goodbye {username}")

def json_response(data):
    return HttpResponse(json.dumps(data, cls=PersonEncoder), content_type="application/json")

def json(request):
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

class Person:
  
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
 
class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)
  
def index2(request):
    people = ["Tom", "Bob", "Sam"]
    id = int(request.GET.get("id", 0))
    # если пользователь найден, возвращаем его
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound("Not Found")
# Чтобы из функции-представления передать данные в шаблон применяется третий параметр функции render, который еще называется context и который представляет словарь. Например, изменим файл views.py следующим образом:
def index(request):
    header = "Данные пользователя"              # обычная переменная
    langs = ["Python", "Java", "C#"]            # список
    user ={"name" : "Tom", "age" : 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж
  
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)
 
def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if(age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
 
def products(request, id):
    return HttpResponse(f"Товар {id}")
 
def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")
 
def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

def connection(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
     
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)

def sum(request, num):
    return HttpResponse(f"<h2>Имя: {num}</h2>")


def a(request):
    return HttpResponse("Hello")

def user(request, name="Undefined", age =0):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def postuser(request):
# получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")


def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)