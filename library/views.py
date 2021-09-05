from django.shortcuts import render
from library.models import Book
from django.http import JsonResponse
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    data = {'books':books.values()}
    print(list(books.values()))

    return JsonResponse(data)


    