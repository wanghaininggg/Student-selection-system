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
        message = '选课成功'
        check_box_list = request.POST.getlist('check_box_list')
        s = courseModels.SelectCourse.objects.filter(selectCourseStatus='1').filter(studentselectcourse__studentSelectCourse_stduent=studentID).values_list('selectCourseClassTime', flat=True)

        for check in check_box_list:
            selectcourse = courseModels.SelectCourse.objects.get(selectCourseID=check)
            if not selectcourse.selectCourseClassTime.id in s:
                b = courseModels.StudentSelectCourse.objects.create(studentSelectCourse_course=selectcourse, studentSelectCourse_stduent=student)
                selectcourse.selectCourseNum = selectcourse.selectCourseNum + 1
                selectcourse.save()
            else:
                message = '时间冲突!'
        courses = courseModels.SelectCourse.objects.filter(selectCourseStatus='1').exclude(studentselectcourse__studentSelectCourse_stduent=studentID)
        selectedcourses = courseModels.SelectCourse.objects.filter(selectCourseStatus='1').filter(studentselectcourse__studentSelectCourse_stduent=studentID)
        return render(request, 'student/studentSelectCourse.html', locals())
    else:
        courses = courseModels.SelectCourse.objects.filter(selectCourseStatus='1').exclude(studentselectcourse__studentSelectCourse_stduent=studentID)
        selectedcourses = courseModels.SelectCourse.objects.filter(selectCourseStatus='1').filter(studentselectcourse__studentSelectCourse_stduent=studentID)
        context = {'courses':courses, 'selectedcourses':selectedcourses}
        return render(request, 'student/studentSelectCourse.html', context)

def studentDeleteCourse(request):
    
    studentID = request.session['user_id']
    student = StudentUser.objects.get(studentID=studentID)

    if request.method == 'POST':
        check_box_list = request.POST.getlist('check_box_list2')

        for check in check_box_list:
            selectcourse = courseModels.SelectCourse.objects.get(selectCourseID=check)
            b = courseModels.StudentSelectCourse.objects.filter(studentSelectCourse_course=selectcourse).filter(studentSelectCourse_stduent=student)
            b.delete()
            selectcourse.selectCourseNum = selectcourse.selectCourseNum - 1
            selectcourse.save()
    return redirect('studentSelectCourse')

