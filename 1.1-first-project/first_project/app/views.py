import locale

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir


locale.setlocale(locale.LC_TIME, 'ru_RU')

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%A %d %B %Y, %H:%M')
    msg = f'Текущее время: {current_time}'
    print(msg)
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директори
    result = f'Список файлов в текущей директории {listdir()}'
    print(result)
    return HttpResponse(result)
