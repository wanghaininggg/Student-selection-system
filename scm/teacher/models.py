from django.db import models
from users import models as user_models
from management import models as management_models
# Create your models here.
class TeacherUser(models.Model):
    sexChoices = (('男','男'),('女','女'))
    teacherID = models.ForeignKey(user_models.User, on_delete=models.CASCADE, verbose_name='教师工号', primary_key=True)
    teacherSex = models.CharField('性别', max_length=1, choices=sexChoices, default='男')
    teacherInstitute = models.ForeignKey(management_models.Institute, on_delete=models.CharField, verbose_name='学院')
    
    def teacher_name(self):
        return self.teacherID.userName
    teacher_name.short_description = '教师姓名'
    teacherName = property(teacher_name)

    class Meta:
        verbose_name='教师'
        verbose_name_plural='教师'

    def __str__(self):
            return self.teacherID.userID