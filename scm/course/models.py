from django.db import models
from management import models as managementModels
from teacher import models as teacherModels
from student import models as studentModels
# Create your models here.
class Course(models.Model):

    gradeChoices = (('2017','2017'),('2016','2016'),('2015','2015'),('2014','2014'),)
    courseID = models.CharField('课程编号', max_length=20, primary_key=True)
    courseName = models.CharField('课程名称', max_length=30)
    courseCredit = models.CharField('课程学分', max_length=3)
    CourseGrade = models.CharField('年级', max_length=4, choices=gradeChoices, default='2017')
    courseMajor = models.ForeignKey(managementModels.Major, on_delete=models.CharField, verbose_name='所属专业')
    courseInstitute = models.ForeignKey(managementModels.Institute, on_delete=models.CharField, verbose_name='所属学院')

    class Meta:
        verbose_name='课程'
        verbose_name_plural='课程'
    
    def __str__(self):
        return self.courseID

class SelectCourse(models.Model):
    
    statusChoices = (('0','未开课'),('1','开课'),)
    selectCourseID = models.CharField('选课编号', max_length=20, primary_key=True)
    selectCourses = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程编号')
    selectCourseTeacher = models.ForeignKey(teacherModels.TeacherUser, on_delete=models.CASCADE, verbose_name='教师工号')
    selectCourseClassroom = models.ForeignKey(managementModels.Classroom, on_delete=models.CASCADE, verbose_name='上课教室', blank=True, null=True)
    selectCourseClassTime = models.ForeignKey(managementModels.ClassTime, on_delete=models.CASCADE, verbose_name='上课时间', blank=True, null=True)
    selectCourseAllNum = models.IntegerField('课程总人数', blank=True, null=True)
    selectCourseNum = models.IntegerField('已选人数', blank=True, null=True)
    selectCourseAddTime = models.DateField('添加时间', auto_now_add=True)
    selectCourseStatus = models.CharField('课程状态', max_length=3, choices=statusChoices, default='0')
    def selectCourse_name(self):
        return self.selectCourses.courseName
    selectCourse_name.short_description = '课程名称'
    selectCourseName = property(selectCourse_name)

    def selectCourse_teacherName(self):
        return self.selectCourseTeacher.teacherName
    selectCourse_teacherName.short_description = '教师姓名'
    selectCoursTeacherName = property(selectCourse_teacherName)

    class Meta:
        ordering = ['-selectCourseAddTime']
        verbose_name = '可选课表'
        verbose_name_plural = '可选课表'

    def __str__(self):
        return self.selectCourseID

class StudentSelectCourse(models.Model):

    studentSelectCourse_course = models.ForeignKey(SelectCourse, on_delete=models.CASCADE, verbose_name='课程')
    studentSelectCourse_stduent = models.ForeignKey(studentModels.StudentUser, on_delete=models.CASCADE, verbose_name='学生学号')
    studentSelectCourse_score =  models.CharField('成绩', max_length=10, blank=True, null=True)
    studentSelectCourseAddTime = models.DateField('添加时间', auto_now_add=True)
    
    def studentSelectCourse_course_courseName(self):
        return self.studentSelectCourse_course.selectCourseName
    studentSelectCourse_course_courseName.short_description = '课程名称'
    studentSelectCourse_courseCourseName = property(studentSelectCourse_course_courseName)

    def studentSelectCourse_course_teacherName(self):
        return self.studentSelectCourse_course.selectCoursTeacherName
    studentSelectCourse_course_teacherName.short_description = '教师姓名'
    studentSelectCourse_courseTeacherName = property(studentSelectCourse_course_teacherName)

    def studentSelectCourse_stduent_studentName(self):
        return self.studentSelectCourse_stduent.studentName 
    studentSelectCourse_stduent_studentName.short_description = '学生姓名'
    studentSelectCourse_stduentStudentName = property(studentSelectCourse_stduent_studentName)
    
    def studentSelectCourse_stduent_studentInstitute(self):
        return self.studentSelectCourse_stduent.studentInstitute
    studentSelectCourse_stduent_studentInstitute.short_description = '学院'
    studentSelectCourse_stduentStudentInstitute = property(studentSelectCourse_stduent_studentInstitute)

    class Meta:
        ordering = ['-studentSelectCourseAddTime']
        verbose_name = '学生选课表'
        verbose_name_plural = '学生选课表'

class TeacherApplyCourse(models.Model):
    statusChoices = (('审核中','审核中'),('批准','批准'),('不同意','不同意'),)
    teacherApplyCourse = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    teacher = models.ForeignKey(teacherModels.TeacherUser, on_delete=models.CASCADE, verbose_name='教师工号')
    status = models.CharField('状态', max_length=3, choices=statusChoices, default='审核中')
    applyCourseAddTime = models.DateField('添加时间', auto_now_add=True)

    def course_name(self):
        return self.teacherApplyCourse.courseName
    course_name.short_description = '课程名称'
    courseName = property(course_name)

    def teacher_name(self):
        return self.teacher.teacherName
    teacher_name.short_description = '教师姓名'
    teacherName = property(teacher_name)

    class Meta:
        ordering = ['applyCourseAddTime']
        verbose_name = '教师申请课程表'
        verbose_name_plural = '教师申请课程表'


