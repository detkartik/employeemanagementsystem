from django.shortcuts import render
from .models import Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer