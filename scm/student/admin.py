from django.contrib import admin
from .models import StudentUser
# Register your models here.
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ('studentID','studentName', 'studentClass', 'studentMajor', 'studentInstitute')
    search_fields = ['studentID']
    list_filter = ('studentClass', 'studentMajor', 'studentInstitute',)
    raw_id_fields = ('studentID',)

admin.site.register(StudentUser, StudentUserAdmin)