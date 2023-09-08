from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='coffee/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CoffeeShop(models.Model):
    street = models.TextField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='shops/', blank=True)
    date_of_creation = models.DateTimeField()
    work_time = models.CharField(max_length=20)

    def __str__(self):
        return self.street


class Worker(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    photo = models.ImageField(upload_to='work/', blank=True)
    salary = models.CharField(max_length=10, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    views = models.CharField(max_length=255, default=0)

    def __str__(self):
        return self.title


class Contacts(models.Model):
    job_title = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, unique=True)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='contact/')

    def __str__(self):
        return self.job_title


class Summary(models.Model):
    genders = (
        ('M', 'Man'),
        ('W', 'Women'),
        ('T', 'Trans')
    )
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=5, choices=genders)
    description = models.TextField()
