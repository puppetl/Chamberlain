from django.db import models

# 员工模型
class Employee(models.Model):
    id = models.AutoField(primary_key=True)  # 员工ID主键自增
    name = models.CharField(max_length=64)  # 员工姓名
    gender = models.CharField(max_length=1)  # 员工性别
    phone = models.CharField(max_length=13)  # 员工手机号
    birthplace = models.CharField(max_length=64)  # 员工籍贯
    birthdate = models.DateField(auto_now=False)  # 员工生日
    joindate = models.DateTimeField(auto_now_add=True)  # 员工加入公司时间 自动添加加入时间
    position = models.CharField(max_length=64)  # 员工职位
    salary = models.FloatField(max_length=13)  # 员工薪资

    def __str__(self):
        return self.name
