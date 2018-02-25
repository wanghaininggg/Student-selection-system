from django.db import models
from users import models as user_models
# Create your models here.
class TeacherUser(models.Model):
    teacherID = models.ForeignKey(user_models.User, on_delete=models.CASCADE, verbose_name='教师工号', primary_key=True)

    def __str__(self):
            return self.teacherID.userID