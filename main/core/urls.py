from django.urls import path
from .views import KeyValueListCreate, KeyValueRetrieveUpdateDestroy

urlpatterns = [
    path('store/', KeyValueListCreate.as_view(), name='store-list-create'),
    path('store/<str:key>/', KeyValueRetrieveUpdateDestroy.as_view(), name='store-detail'),
]
