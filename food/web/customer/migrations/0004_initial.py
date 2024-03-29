# Generated by Django 3.2 on 2021-05-09 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_auto_20210509_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='menu_id/')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(blank=True, related_name='oder', to='customer.foodForm')),
            ],
        ),
        migrations.AddField(
            model_name='foodform',
            name='loai',
            field=models.ManyToManyField(related_name='item', to='customer.Style'),
        ),
    ]
