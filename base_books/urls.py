from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import BookViewSet,AuthorViewSet,home_view,book_list,book_reading_detail

router = DefaultRouter()
router.register('books',BookViewSet,basename='book')


urlpatterns = [
    path('',home_view,name='home'),
    path('books/',book_list,name='book_list'),
    path('reading/<int:pk>/',book_reading_detail,name='book_reading_detail'),
    path('api/',include(router.urls))
]