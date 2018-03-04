from django import forms
from course.models import TeacherApplyCourse

class TeacherApplyCourseForm(forms.ModelForm):
    class Meta:
    	model = TeacherApplyCourse
    	fields = ['teacherApplyCourse','teacher']
    	labels = {'teacherApplyCourse':'课程编号'}