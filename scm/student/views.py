from django.shortcuts import render
from .models import StudentUser
from course import models as courseModels
# Create your views here.
def studentIndex(request):
	pass
	return render(request, 'student/studentIndex.html')

def studentInformation(request):
	student = StudentUser.objects.get(studentID=request.session['user_id'])
	context = {'student':student}
	return render(request, 'student/studentInformation.html', context)

def studentScore(request):
	scores = courseModels.StudentSelectCourse.objects.filter(studentSelectCourse_stduent=request.session['user_id'])
	context = {'scores':scores}
	return render(request, 'student/studentScore.html', context)

def studentSelectCourse(request):
	pass
	return render(request, 'student/studentSelectCourse.html')