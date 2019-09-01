from django.shortcuts import render
from accounts.forms import RegisterForm


def register(request):
    # 회원가입 정보가 서버로 전달됬을 때
    if request.method == 'POST':
        print("2222222222222222222222222222")
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # 폼 객체에 지정된 모델 확인 후 모델 객체 만듦.
            # commit=False : 데이터베이스에 저장하는 것이 아닌 메모리 상에 객체 만듦.
            new_user = user_form.save(commit=False)
            # 비밀번호 암호화 처리 저장
            new_user.set_password(user_form.cleaned_data['password'])
            # 데이터베이스에 저장
            new_user.save()
            # 회원가입 완료 후 register_done.html로 렌더링
            print("4444444444444444444444444444444")
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    # 회원가입 정보가 서버로 전달되지 않았을 때
    else:
        print("333333333333333333333333333333")
        user_form = RegisterForm()
    # 회원가입 페이지
    print("11111111111111111111111111")
    return render(request, 'registration/register.html', {'form':user_form})