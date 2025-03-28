from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subs')
    title = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="products")
    size = models.ManyToManyField(Size, blank=True, null=True, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="information")
    text = models.TextField()

    def __str__(self):
        return self.text[:30]
