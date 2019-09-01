from django.contrib.auth.models import User
from django import forms

# 회원가입 폼 - forms.ModelForm 을 상속 받음
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    # 필드 지정
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # 유효성 검사 - password, password2 같은지 비교

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']