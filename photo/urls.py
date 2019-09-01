from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo

# app_name : 네임스페이스로 사용되는 값
# 템플릿에서 url 템플릿 태그를 사용할 때 app_name값이 설정되어 있다면
# [app_name:URL패턴이름] 형태로 사용
app_name = 'photo'

urlpatterns = [
    # 함수형 뷰
    path('', photo_list, name='photo_list'),
    # 클래스형 뷰
    # 제네릭 뷰인 DetailView는 views.py가 아닌 urls.py에서 인라인 코드로 작성할 수 있다.
    # path함수에 인수로 전달할 때는 as_view안에 클래스 변수들을 설정해 사용.
    path('detail/<int:pk>/',
         DetailView.as_view(model=Photo, template_name='photo/detail.html'),
         name = 'photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name = 'photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name = 'photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name = 'photo_update'),
]