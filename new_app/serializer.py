from rest_framework import serializers

from new_app.models import EmployeeDetail


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = ('designation', 'salary')
