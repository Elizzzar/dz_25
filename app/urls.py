from django.urls import path
from .views import IceCreamListView, IceCreamCreateView
urlpatterns = [
    path('', IceCreamListView.as_view(), name='ice_cream_list'),
    path('create/', IceCreamCreateView.as_view(), name='ice_cream_create'),
]