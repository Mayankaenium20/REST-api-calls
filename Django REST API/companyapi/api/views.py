from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from api.models import Company, Employee
from api.serializers import CompanySerializers, EmployeeSerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):            #this function includes all the methods
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    permission_classes = [IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
