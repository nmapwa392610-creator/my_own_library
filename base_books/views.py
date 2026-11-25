from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book,Author,BookReading
from .serializer import BookSerializer,AuthorSerializer,BookReadingSerializer
from rest_framework import viewsets
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.viewsets import ModelViewSet
# Create your views here.


def home_view(request):
    books = Book.objects.all().order_by('id')
    paginator = Paginator(books,10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'book': page_obj})


def book_list(request):
    books = Book.objects.all().order_by('id')

    query = request.GET.get('q')
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    paginator = Paginator(books,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'book_list.html',{'book':page_obj})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

    def get_permission(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookReadingViewSet(viewsets.ModelViewSet):
    queryset = BookReading.objects.all()
    serializer_class = BookReadingSerializer