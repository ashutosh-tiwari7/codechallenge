from django.urls import path
from .views import ApartmentView


urlpatterns = [
    path('apartments/', ApartmentView.as_view(), name='apartments'),
]