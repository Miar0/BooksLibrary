from django.urls import path
from core.views import *

urlpatterns = [
    path('books/', BookListCreateView.as_view()),
    path('author/', AuthorListCreateView.as_view()),
    path('genre/', GenreListCreateView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),
    path('author/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view()),
    path('genre/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view()),
]
