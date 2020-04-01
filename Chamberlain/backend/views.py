from django.shortcuts import render
from django.views import View  # 类视图
from backend.models import Employee
from django.http import HttpResponse
class EmployeeView(View):

    def get(self,request):
        employees = Employee.objects.all()
        # id = employee.id
        # name = employee.name
        # gender = employee.gender
        # phone = employee.phone
        # birthplace = employee.birthplace
        # joindate = employee.joindate
        # position = employee.position
        # salary = employee.salary
        pass
    def post(self, request):
        pass
