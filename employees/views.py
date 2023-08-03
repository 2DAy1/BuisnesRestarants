
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from core.accounts import UserSerializer  # Corrected import statement


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MenuVotingView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = serializer.save()
        # Handle the logic for menu voting here based on the employee's choice.
        # You might want to create additional models for menu voting and handle
        # the associations between employees and their menu choices.

        return Response({'message': 'Menu vote recorded successfully.'})
