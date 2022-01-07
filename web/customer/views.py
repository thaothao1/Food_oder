from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from .models import MenuItem, Category, OrderModel 
from django.core.mail import  send_mail



class Index(View):
    def get(self, request , *args , **kwargs):
        return render(request , 'customer/index.html')
class About(View):
    def get(self , request , *args , **Kwargs):
        return render(request, 'customer/about.html')   
class Home(View):
    def get(self , request , *args , **Kwargs):
        return render(request, 'customer/Home.html')  
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'customer/register.html', {'form': form})

class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        seafood = MenuItem.objects.filter(category__name__contains='seafood')
        beef = MenuItem.objects.filter(category__name__contains='beef')
        chicken = MenuItem.objects.filter(category__name__contains='chicken')
        pork = MenuItem.objects.filter(category__name__contains='pork')
        vegetable = MenuItem.objects.filter(category__name__contains='vegetable')
        # pass into context
        context = {
            'seafood': seafood,
            'beef':beef,
            'chicken': chicken,
            'pork': pork,
            'vegetable' : vegetable,
        }

        # render the template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip')
        street = request.POST.get('street')
        state = request.POST.get('state')
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)


            price = 0
            item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create( 
            name=name, 
            price=price,  
            email=email, 
            street=street, 
            city=city, 
            state=state, 
            zip_code=zip_code
            )
        order.items.add(*item_ids)
        
       # After everything is done, send confirmation email to user
        body = ('Thank you for your order!  Your food is being made and will be delivered soon!\n'
        f'Your total: {price}\n'
        'Thank you again for your order!')
        send_mail(
            'Thank You For Your Order!',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )
        context={
            'items': order_items['items'],
            'price': price,
        }


        return render(request, 'customer/order_aconfirmation.html' , context )
class Menu(View):
    def get(seft , request , *args , **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }
        return render(request , 'customer/menu.html' , context)

class MenuSearch(View):
    def get(self , request , *args , **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)|
            Q(pk__icontains=query)
        )
        context ={
            'menu_items': menu_items
        }
        return render(request ,'customer/menu.html' , context)
