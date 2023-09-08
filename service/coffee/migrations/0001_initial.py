# Generated by Django 4.2.2 on 2023-06-06 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('date_of_creation', models.DateTimeField()),
                ('work_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='contact/')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('coffee_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee.coffeeshop')),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='coffee/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee.categories')),
            ],
        ),
    ]