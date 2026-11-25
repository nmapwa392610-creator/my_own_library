from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import BookViewSet,AuthorViewSet,home_view,book_list

router = DefaultRouter()
router.register('books',BookViewSet,basename='book')


urlpatterns = [
    path('',home_view,name='home'),
    path('books/',book_list,name='book_list'),
    path('api/',include(router.urls))
]