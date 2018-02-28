from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'input-block-level','placeholder':'用户名'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'input-block-level', 'placeholder':'密码'}))
    captcha = CaptchaField(label='验证码')
