from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('userID', 'userName', 'userPassword', 'userIdentity', 'userAddTime')
	search_fields = ['userID']
	list_filter = ('userIdentity',)

admin.site.register(User, UserAdmin)
admin.site.site_header = '云南师范大学学生选课管理系统'
admin.site.site_title = '云南师范大学学生选课管理系统'
