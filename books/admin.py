from django.contrib import admin

from .models import Category, Author, Book, Review


#
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_per_page = 25


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',) }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
