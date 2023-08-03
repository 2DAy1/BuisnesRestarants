from django.urls import path
from .views import MenuCreateView, MenuRetrieveView

urlpatterns = [
    path('/', MenuCreateView.as_view(), name='menu-create'),
    path('/<int:pk>/', MenuRetrieveView.as_view(), name='menu-retrieve'),
]