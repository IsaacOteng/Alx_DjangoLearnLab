from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Apply authentication + custom permissions
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   # Automatically assign the logged-in user as owner