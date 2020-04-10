from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 员工模型
class Employee(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="员工ID")  # 员工ID主键自增
    name = models.CharField(max_length=64, verbose_name="姓名")  # 员工姓名
    gender = models.CharField(max_length=1, verbose_name="性别")  # 员工性别
    phone = models.CharField(max_length=13, verbose_name="手机号")  # 员工手机号
    birthplace = models.CharField(max_length=64, verbose_name="籍贯")  # 员工籍贯
    birthdate = models.DateField(auto_now=False, verbose_name="生日")  # 员工生日
    joindate = models.DateTimeField(auto_now_add=True, verbose_name="加入时间")  # 员工加入公司时间 自动添加加入时间
    position = models.CharField(max_length=64, verbose_name="职位")  # 员工职位
    salary = models.FloatField(max_length=13, verbose_name="薪资")  # 员工薪资

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = verbose_name


class UserInfo(AbstractUser):
# class UserInfo(models.Model):
    tel = models.CharField(max_length=32,verbose_name="电话")
    avatar = models.FileField(upload_to="avatars/", default="avatars/timg.jpg", verbose_name="头像")


class Room(models.Model):
    """房间表"""
    caption = models.CharField(max_length=32,verbose_name="房间名称")
    num = models.IntegerField(verbose_name="容纳人数")  # 容纳人数

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "房间信息"
        verbose_name_plural = verbose_name


class Book(models.Model):
    """房间预订"""
    user = models.ForeignKey(to="UserInfo",on_delete=models.CASCADE)
    room = models.ForeignKey(to="Room",on_delete=models.CASCADE)
    date = models.DateField()
    time_choice = (
        (1, "0:00-1:00"),
        (2, "1:00-2:00"),
        (3, "2:00-3:00"),
        (4, "3:00-4:00"),
        (5, "4:00-5:00"),
        (6, "5:00-6:00"),
        (7, "6:00-7:00"),
        (8, "7:00-8:00"),
        (9, "8:00-9:00"),
        (10, "9:00-10:00"),
        (11, "10:00-11:00"),
        (12, "11:00-12:00"),
        (13, "12:00-13:00"),
        (14, "13:00-14:00"),
        (15, "14:00-15:00"),
        (16, "15:00-16:00"),
        (17, "16:00-17:00"),
        (18, "17:00-18:00"),
        (19, "18:00-19:00"),
        (20, "19:00-20:00"),
        (21, "20:00-21:00"),
        (22, "21:00-22:00"),
        (23, "22:00-23:00"),
        (24, "23:00-0:00"),
        (25, "0:00-12:00"),
        (26, "0:00-24:00"),
   
    )

    time_id = models.IntegerField(choices=time_choice)

    def __str__(self):
        return str(self.user)+"预定了"+str(self.room)

    class Meta:
        verbose_name = "预定信息"
        verbose_name_plural = verbose_name
        unique_together = (
            ("room","date","time_id"),  # 这三个字段联合唯一，防止重复预订
        )
