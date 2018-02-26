from django.db import models
from users import models as user_models
from management import models as management_models
# Create your models here.
class StudentUser(models.Model):
    sexChoices = (('男','男'),('女','女'))

    studentID = models.ForeignKey(user_models.User, on_delete=models.CASCADE, verbose_name='学生学号', primary_key=True)
    studentSex = models.CharField('性别', max_length=1, choices=sexChoices, default='男')
    studentInstitute = models.ForeignKey(management_models.Institute, on_delete=models.CharField, verbose_name='学院')
    studentMajor = models.ForeignKey(management_models.Major, on_delete=models.CharField, verbose_name='专业')
    studentClass = models.ForeignKey(management_models.Class, on_delete=models.CharField, verbose_name='班级')

    def student_name(self):
        return self.studentID.userName
    student_name.short_description = '学生姓名'
    studentName = property(student_name)
    
    class Meta:
        verbose_name='学生'
        verbose_name_plural='学生'

    def __str__(self):
            return self.studentID.userID