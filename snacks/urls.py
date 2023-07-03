from django.urls import path
from .views import SnacksList, SnackDetail

urlpatterns = [
    path('', SnacksList.as_view(), name='snacks_list'),
    path('/<int:pk>/', SnackDetail.as_view(), name='snack_detail'),
]