from django.db import models
class foodForm(models.Model):
    name = models.CharField(max_length = 100)
    nguyenlieu = models.TextField()
    soche = models.TextField()
    thuchien = models.TextField()
    cachdung = models.TextField()
    machnho = models.TextField()
    image = models.ImageField(upload_to='menu_id/')
    video = models.FileField(upload_to='video/')
    loai = models.ManyToManyField('Style' , related_name='item')
    price = models.DecimalField(max_digits=7, decimal_places=3 )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'foodForm'
        verbose_name_plural = 'foodForms'

class Style(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    price = models.DecimalField(max_digits=7, decimal_places=3 )
    items = models.ManyToManyField('foodForm' , related_name='order' )
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50, blank=True)
    SDT = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'




