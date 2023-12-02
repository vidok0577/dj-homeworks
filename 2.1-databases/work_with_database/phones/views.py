from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    get_sort = ['name', 'min_price', 'max_price', None].index(request.GET.get('sort'))
    sort = ['name', 'price', '-price', 'name'][get_sort]
    phones = Phone.objects.all().order_by(sort)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
