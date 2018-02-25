from django.db import models
from users import models as user_models
# Create your models here.
class StudentUser(models.Model):
    studentID = models.ForeignKey(user_models.User, on_delete=models.CASCADE, verbose_name='学生学号', primary_key=True)

    def __str__(self):
            return self.studentID.userID