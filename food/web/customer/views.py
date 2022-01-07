# from typing_extensions import ParamSpec
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.core.mail import  send_mail
from django.core.paginator import EmptyPage, Paginator
from .models import  OrderModel , foodForm , Style 





class Index(View):
    def get(self, request , *args , **kwargs):
        return render(request , 'customer/index.html')
class About(View):
    def get(self , request , *args , **Kwargs):
       return render(request, 'customer/about.html')   
class Home(View):
    def get(self, request , *args , **kwargs):
        return render(request , 'customer/Home.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'customer/register.html', {'form': form})

class Menu(View):
    def get(self , request , *args , **kwargs):
        menu_items = foodForm.objects.all()
        p = Paginator(menu_items, 20)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        

        context = {
            'menu_items': page
        }
        return render(request, 'customer/menu.html' , context)


class MenuSearch(View):
    def get( self , request , *args , **kwargs):
        query = self.request.GET.get("q")
        menu_items = foodForm.objects.filter(
            Q(name__icontains=query)|
            Q(price__icontains=query)|
            Q(id__icontains=query)
        )
        context = {
            'menu_items':menu_items
        }  
        return render(request, 'customer/menu.html' , context)
def DetailsMenu(request , id):
    menu = foodForm.objects.get(id = id )
    
    return render(request,'customer/DetailsMenu.html', {'menu':menu})
    
class Order(View):

    def get(self, request, *args, **kwargs):
        menu_itemss = foodForm.objects.all()
        p = Paginator(menu_itemss, 10)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        
        context = {
            'menu_itemss': page
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        SDT = request.POST.get('SDT')
        street = request.POST.get('street')
        city = request.POST.get('city')
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
        for item in items:
            menu_itemss = foodForm.objects.get(id =int(item))
            item_data = {
                'id': menu_itemss.pk,
                'name': menu_itemss.name,
                'price': menu_itemss.price,
            }
            order_items['items'].append(item_data)
        
        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])
        
        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            SDT=SDT,
            street=street,
            city=city,
          
            )
        order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price
        
        }

        return render(request, 'customer/order_confirmation.html', context)

class OrderSearch(View):
    def get( self , request , *args , **kwargs):
        query = self.request.GET.get("q")
        menu_itemss = foodForm.objects.filter(
            Q(name__icontains=query)|
            Q(price__icontains=query)|
            Q(id__icontains=query)
        )
        context = {
            'menu_itemss':menu_itemss
        }  
        return render(request, 'customer/order.html' , context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        SDT = request.POST.get('SDT')
        street = request.POST.get('street')
        city = request.POST.get('city')
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
        for item in items:
            menu_itemss = foodForm.objects.get(id__contains=int(item))
            item_data = {
                'id': menu_itemss.pk,
                'name': menu_itemss.name,
                'price': menu_itemss.price,
            }
            order_items['items'].append(item_data)
        
        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])
        
        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            SDT=SDT,
            street=street,
            city=city,
          
            )
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'customer/order_confirmation.html', context)

   
