"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from customer.views import Index , About , register  , Home , Menu , MenuSearch , DetailsMenu , Order , OrderSearch
from  customer import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/' , admin.site.urls ),

    path('Home/', Home.as_view(), name='home'),
    path('', Index.as_view() , name='index'),
    path('order/', Order.as_view() , name='order'),
    path('order/search/', OrderSearch.as_view() , name = 'Order-search'),
    path( 'menu/', Menu.as_view() , name='Menu'),
    path('Menu/search/', MenuSearch.as_view() , name = 'Menu-search'),
    path( 'about/' , About.as_view() , name = 'about'),
    path('register/', views.register, name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="customer/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='menu'),name='logout'),
    path('<int:id>/',views.DetailsMenu , name = 'DetailsMenu'),
   
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)