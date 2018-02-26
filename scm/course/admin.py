from django.contrib import admin
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'courseName', 'courseCredit', 'courseMajor', 'coutseInstitute')
    search_fields = ['courseID', 'courseName']
    list_filter = ('courseMajor', 'coutseInstitute')
    
admin.site.register(Course, CourseAdmin)