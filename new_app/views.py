from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from new_app.models import EmployeeDetail
from new_app.serializer import EmployeeDetailSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def employeeDetails(request):
    if request.method == "GET":
        details = EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(details, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = EmployeeDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id):
    try:
        employee = EmployeeDetail.objects.get(id=id)
    except EmployeeDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeDetailSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_204_NO_CONTENT)
