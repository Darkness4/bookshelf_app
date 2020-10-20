from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from bookshelf.models import Book
from bookshelf.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["author"]
    search_fields = ["title", "author"]
