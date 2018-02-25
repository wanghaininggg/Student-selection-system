from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)
admin.site.site_header = '云南师范大学学生选课管理系统'
admin.site.site_title = '云南师范大学学生选课管理系统'