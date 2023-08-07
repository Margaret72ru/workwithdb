from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = 'name'
    if request.GET.keys().__contains__("sort"):
        sort = str(request.GET["sort"]).lower()
    data_all = Phone.objects.all()
    data = None
    if sort == 'min_price':
        data = data_all.order_by('price').values()
    elif sort == 'max_price':
        data = data_all.order_by('price').reverse().values()
    else:
        data = data_all.order_by(sort).values()
    context = {'phones': data}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    data = Phone.objects.filter(slug=slug).first()
    context = {'phone': data}
    return render(request, template, context)
