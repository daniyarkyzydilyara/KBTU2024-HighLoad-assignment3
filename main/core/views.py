from rest_framework import generics
from core.models import KeyValue
from .serializers import KeyValueSerializer


class KeyValueListCreate(generics.ListCreateAPIView):
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer


class KeyValueRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer
    lookup_field = 'key'
