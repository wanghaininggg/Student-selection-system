"""scm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from users import views as usersView
from student import views as studentView
from teacher import views as teacherView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', usersView.index, name='index'),
    path('login/', usersView.login, name='login'),
    path('logout/', usersView.logout, name='logout'),
    path('captcha', include('captcha.urls')),

    path('teacher/', teacherView.teacherIndex, name='teacherIndex'),
    path('teacherInformation', teacherView.teacherInformation, name='teacherInformation'),
    path('teacherManagement/', teacherView.teacherManagement, name='teacherManagement'),
    path('teacherCourse/', teacherView.teacherCourse, name='teacherCourse'),
    path('teacherManagementClass/<int:classID>', teacherView.teacherManagementClass, name='teacherManagementClass'),


    path('student/', studentView.studentIndex, name='studentIndex'),
    path('studentInformation/', studentView.studentInformation, name='studentInformation'),
    path('studentScore/', studentView.studentScore, name='studentScore'),
    path('studentSelectCourse/',studentView.studentSelectCourse, name='studentSelectCourse'),
    path('studentDeleteCourse/', studentView.studentDeleteCourse, name='studentDeleteCourse'),
]
