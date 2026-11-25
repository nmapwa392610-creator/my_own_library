from django.contrib import admin
from .models import Author,BookReading,Book
# Register your models here.
admin.site.register(Author)
admin.site.register(BookReading)
admin.site.register(Book)