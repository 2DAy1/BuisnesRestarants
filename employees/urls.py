from django.urls import path
from .views import EmployeeCreateView, MenuVotingView

urlpatterns = [
    path('/', EmployeeCreateView.as_view(), name='employee-create'),
    path('vote/', MenuVotingView.as_view(), name='menu-vote'),
]