from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about_author = models.TextField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=125)
    shortDescription = models.CharField(max_length=250)
    longDescription = models.TextField()
    image = models.ImageField(upload_to='images/book', null=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title} by {self.title}'


class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='images/review', null=True)

    def __str__(self):
        return f'{self.body[:25]} from {self.book}'
