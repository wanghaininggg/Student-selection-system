from django.contrib import admin
from .models import Course, SelectCourse, StudentSelectCourse, TeacherApplyCourse
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'courseName', 'CourseGrade','courseCredit', 'courseMajor', 'courseInstitute')
    search_fields = ['courseID', 'courseName']
    list_filter = ('CourseGrade', 'courseMajor', 'courseInstitute')
    
admin.site.register(Course, CourseAdmin)

class SelectCourseAdmin(admin.ModelAdmin):
    list_display = ('selectCourseID', 'selectCourses', 'selectCourseName', 'selectCourseTeacher', 'selectCoursTeacherName', 'selectCourseClassTime', 'selectCourseClassroom', 'selectCourseAllNum', 'selectCourseNum', 'selectCourseAddTime', 'selectCourseStatus')
    raw_id_fields = ('selectCourses', 'selectCourseTeacher')
    list_filter = ('selectCourses','selectCourseClassroom', 'selectCourseClassTime')
    search_fields = ['selectCourseID', 'selectCourseTeacher__teacherID__userID', 'selectCourses__courseID','selectCourseTeacher__teacherID__userName']
    list_editable =('selectCourseClassroom', 'selectCourseClassTime', 'selectCourseAllNum', 'selectCourseNum', 'selectCourseStatus')
admin.site.register(SelectCourse, SelectCourseAdmin)

class StudentSelectCourseAdmin(admin.ModelAdmin):
    list_display = ('studentSelectCourse_course', 'studentSelectCourse_courseCourseName', 'studentSelectCourse_stduent', 'studentSelectCourse_stduentStudentName', 'studentSelectCourse_stduentStudentInstitute', 'studentSelectCourse_courseTeacherName', 'studentSelectCourse_score', 'studentSelectCourseAddTime')
    raw_id_fields = ('studentSelectCourse_course', 'studentSelectCourse_stduent')
    list_filter = ('studentSelectCourse_stduent__studentInstitute','studentSelectCourse_course__selectCourses__courseName', 'studentSelectCourse_course__selectCourseTeacher')
    search_fields = ['studentSelectCourse_course__selectCourses__courseName', 'studentSelectCourse_stduent__studentID__userID']
    list_editable =('studentSelectCourse_score', )
admin.site.register(StudentSelectCourse, StudentSelectCourseAdmin)

class TeacherApplyCourseAdmin(admin.ModelAdmin):
    list_display = ('teacherApplyCourse', 'courseName', 'teacher', 'teacherName', 'status','applyCourseAddTime')
    actions = ['approveApplyCourse', 'disagreeApplyCourse', 'reviewApplyCourse']
    def approveApplyCourse(self, request, queryset):
           rows_updated = queryset.update(status='批准')
           message = "%s 条申请批准成功！" %rows_updated
           self.message_user(request, message)
    approveApplyCourse.short_description = "批准所选的 教师申请课程表"

    def disagreeApplyCourse(self, request, queryset):
           rows_updated = queryset.update(status='不同意')
           message = "%s 条申请驳回成功！" %rows_updated
           self.message_user(request, message)
    disagreeApplyCourse.short_description = "否定所选的 教师申请课程表"

    def reviewApplyCourse(self, request, queryset):
           rows_updated = queryset.update(status='审核中')
           message = "%s 条状态改为审核中！" %rows_updated
           self.message_user(request, message)
    reviewApplyCourse.short_description = "审核所选的 教师申请课程表"

admin.site.register(TeacherApplyCourse, TeacherApplyCourseAdmin)