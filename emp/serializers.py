from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField()

    def get_employee(self, obj):
        return ' '.join([obj.first_name, obj.last_name])
    
    class Meta:
        model = Employee
        fields = ('id','employee','manager')