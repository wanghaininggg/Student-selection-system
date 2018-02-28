from django.contrib import admin
from .models import Institute, Major, Class, Classroom, ClassTime
# Register your models here.

class InstituteAdmin(admin.ModelAdmin):
    list_display = ('instituteID', 'instituteName', 'institutePhohe', 'instituteMailbox')
    list_editable = ('institutePhohe', 'instituteMailbox')
    search_fields = ['instituteID', 'instituteName']
    list_per_page = 30

class MajorAdmin(admin.ModelAdmin):
    list_display = ('majorID', 'majorName', 'majorInstitute')
    search_fields = ['majorID', 'majorName']
    list_filter = ('majorInstitute',)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('classID', 'classGrade', 'className', 'classMajor', 'classInstitute')
    search_fields = ['classID']    
    list_filter = ('classMajor', 'classInstitute')

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroomName',)

admin.site.register(Institute, InstituteAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(ClassTime)