from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from .forms import UserForm
# Create your views here.
def index(request):
    pass
    return render(request, 'users/index.html')

def login(request):
    if request.session.get('is_login', None):
        return redirect('index')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写内容'
        if login_form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            try:
                user = User.objects.get(userID=username)
                if user.userPassword == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.userID
                    request.session['user_name'] = user.userName
                    request.session['user_identity'] = user.userIdentity
                    return redirect('index')
                else:
                    message = '密码不正确'
            except:
                message = "用户名不存在！"
        else:
            return render(request, 'users/login.html', locals())
    else:
        login_form = UserForm()
    return render(request, 'users/login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('index')
    request.session.flush()
    return redirect("/")