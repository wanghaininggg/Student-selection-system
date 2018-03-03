from django.contrib import admin
from .models import Course, SelectCourse, StudentSelectCourse
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'courseName', 'CourseGrade','courseCredit', 'courseMajor', 'courseInstitute')
    search_fields = ['courseID', 'courseName']
    list_filter = ('CourseGrade', 'courseMajor', 'courseInstitute')
    
admin.site.register(Course, CourseAdmin)

class SelectCourseAdmin(admin.ModelAdmin):
    list_display = ('selectCourseID', 'selectCourses', 'selectCourseName', 'selectCourseTeacher', 'selectCoursTeacherName', 'selectCourseClassTime', 'selectCourseClassroom', 'selectCourseAddTime')
    raw_id_fields = ('selectCourses', 'selectCourseTeacher')

admin.site.register(SelectCourse, SelectCourseAdmin)

class StudentSelectCourseAdmin(admin.ModelAdmin):
    list_display = ('studentSelectCourse_course', 'studentSelectCourse_courseCourseName', 'studentSelectCourse_stduent', 'studentSelectCourse_stduentStudentName', 'studentSelectCourse_stduentStudentInstitute', 'studentSelectCourse_courseTeacherName', 'studentSelectCourse_score', 'studentSelectCourseAddTime')
    raw_id_fields = ('studentSelectCourse_course', 'studentSelectCourse_stduent')
    list_filter = ('studentSelectCourse_stduent__studentInstitute','studentSelectCourse_course__selectCourses__courseName', 'studentSelectCourse_course__selectCourseTeacher')
    search_fields = ['studentSelectCourse_course__selectCourses__courseName', 'studentSelectCourse_stduent__studentID__userID']
    list_editable =('studentSelectCourse_score', )
admin.site.register(StudentSelectCourse, StudentSelectCourseAdmin)