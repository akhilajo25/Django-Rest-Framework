from django.urls import path, include
from library.views import book_list
urlpatterns = [
    path('list/', book_list, name='book-list'),

]
