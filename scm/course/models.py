from django.db import models
from management import models as managementModels
# Create your models here.
class Course(models.Model):
    courseID = models.CharField('课程编号', max_length=20, primary_key=True)
    courseName = models.CharField('课程名称', max_length=30)
    courseCredit = models.CharField('课程学分', max_length=3)
    courseMajor = models.ForeignKey(managementModels.Major, on_delete=models.CharField, verbose_name='所属专业')
    coutseInstitute = models.ForeignKey(managementModels.Institute, on_delete=models.CharField, verbose_name='所属学院')

    class Meta:
        verbose_name='课程'
        verbose_name_plural='课程'
    
    def __str__(self):
        return self.courseID
