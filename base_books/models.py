from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='covers/',blank=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class BookReading(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    chapter = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f'чтение {self.book.title}'
