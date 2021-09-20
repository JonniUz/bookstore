from django import forms
from .models import Book, Author, Category, Review


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'about_author')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'shortDescription', 'longDescription', 'image', 'author', 'category')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', 'image')
