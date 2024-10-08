from rest_framework import serializers
from api.models import Company, Employee

class CompanySerializers(serializers.HyperlinkedModelSerializer):

    # company_id = serializers.ReadOnlyField()                    #to avoid any type of updates over the primary key

    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"