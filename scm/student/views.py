from django.shortcuts import render
from .models import StudentUser
from course import models as courseModels
from django.shortcuts import redirect
# Create your views here.
def studentIndex(request):
    pass
    return render(request, 'student/studentIndex.html')

def studentInformation(request):
    student = StudentUser.objects.get(studentID=request.session['user_id'])
    context = {'student':student}
    return render(request, 'student/studentInformation.html', context)

def studentScore(request):
    a,b,c,d,e = 0.0,0.0,0.0,0.0,0
    scores = courseModels.StudentSelectCourse.objects.filter(studentSelectCourse_stduent=request.session['user_id'])
  
    for score in scores:
        if score.studentSelectCourse_score is None:
            pass
        else:
            if int(score.studentSelectCourse_score) > 90:
                a = a+1
            elif int(score.studentSelectCourse_score) > 80:
            	b = b+1
            elif int(score.studentSelectCourse_score) >60:
            	c = c+1
            else:
            	d = d +1
            e = e+1
    if e != 0:
        a = round(a/e, 2)*100
        b = round(b/e, 2)*100
        c = round(c/e, 2)*100
        d = round(d/e, 2)*100
    context = {'scores':scores,'a':a,'b':b,'c':c,'d':d}
    return render(request, 'student/studentScore.html', context)

def studentSelectCourse(request):
    
    studentID = request.session['user_id']
    student = StudentUser.objects.get(studentID=studentID)
    if request.method == 'POST':
        check_box_list = request.POST.getlist('check_box_list')

        for check in check_box_list:
            selectcourse = courseModels.SelectCourse.objects.get(selectCourseID=check)
            b = courseModels.StudentSelectCourse.objects.create(studentSelectCourse_course=selectcourse, studentSelectCourse_stduent=student)
        return redirect('studentScore')
    else:
        courses = courseModels.SelectCourse.objects.exclude(studentselectcourse__studentSelectCourse_stduent=studentID)
        context = {'courses':courses}
        return render(request, 'student/studentSelectCourse.html', context)

def studentDeleteCourse(request):

    studentID = request.session['user_id']
    student = StudentUser.objects.get(studentID=studentID)

