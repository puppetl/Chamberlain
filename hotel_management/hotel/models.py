from django.db import models


# Create your models here.
class Article(models.Model):
    # 房间号
    room_id = models.AutoField(primary_key=True)
    # 入住人员姓名
    room_name = models.TextField()
    # 入住时间
    room_timestart = models.TextField()
    # 结束时间
    room_timeover = models.TextField()


    def __str__(self):
        return self.article_id
