from django.db import models


# Create your models here.
class Institute(models.Model):

    instituteID = models.CharField('学院编号', max_length=20, primary_key=True)
    instituteName = models.CharField('学院名称', max_length=30)
    institutePhohe = models.CharField('学院电话', max_length=20, null=True, blank=True)
    instituteMailbox = models.EmailField('学院邮箱', null=True, blank=True)
    instituteInformation = models.CharField('学院信息', max_length=1000, null=True, blank=True)
 
    class Meta:
        verbose_name='学院'
        verbose_name_plural='学院'
    def __str__(self):
        return self.instituteName
            

class Major(models.Model):

    majorID = models.CharField('专业编号', max_length=20, primary_key=True)
    majorName = models.CharField('专业名称', max_length=30)
    majorInstitute= models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name='所在学院')
    majorInformation = models.CharField('学院信息', max_length=1000, null=True, blank=True)    
    
    class Meta:
        verbose_name='专业'
        verbose_name_plural='专业'
    def __str__(self):
        return self.majorName

class Class(models.Model):
    classID = models.CharField('班级编号', max_length=20, primary_key=True)
    className = models.CharField('班级名称', max_length = 30)
    classGrade = models.CharField('班级年级', max_length = 4, default='2017')
    classMajor = models.ForeignKey(Major, on_delete=models.CASCADE, verbose_name='所在专业')
    classInstitute = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name='所在学院')
    
    class Meta:
        verbose_name='班级'
        verbose_name_plural='班级'

    def __str__(self):
        return self.className

class Classroom(models.Model):
    
    classroomName = models.CharField('教室名称', max_length=30)
    
    class Meta:
        verbose_name='教室'
        verbose_name_plural='教室'

    def __str__(self):
        return self.classroomName           

class ClassTime(models.Model):

    classTime = models.CharField('上课时间', max_length=30)

    class Meta:
        verbose_name='上课时间'
        verbose_name_plural='上课时间'

    def __str__(self):
        return self.classTime
