from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):

    # [author] : ForeignKey를 사용하여 User 테이블과 관계를 만듬.
    # User: 장고에서 기본적으로 사용하는 사용자 모델이다.
    # on_delete=models.CASCADE : 연결된 모델이 삭제될 경우 해당 하위 객체도 같이 삭제
    # related_name : 연결된 객체에서 하위 객체의 목록을 부를 때 사용할 이름
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')

    # [photo]
    # upload_to : 사진이 업로드 될 경로. 만약 업로드가 되지 않을 경우 default 값으로 대체
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')

    # [text] : 사진에 대한 설명 저장 텍스트 필드. 문자열 길이에 제한 없음.
    text = models.TextField()

    # [created] 글 작성 일을 저장하기 위한 날짜시간 필드
    # auto_now_add : 객체가 추가될 때 자동으로 값 설정
    created = models.DateTimeField(auto_now_add=True)

    # [updated] : 글 수정일을 저장하기 위한 날짜 필드.
    # auto_now : 객체가 수정될 때마다 자동으로 값을 설정.
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering 클래스 변수 : 해당 모델의 객체들을 어떤 기준으로 정렬할 것인지 설정하는 옵션
        # -updated : 글 수정 시간의 내림차순으로 정렬
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime('%Y-%m-%d %H:%M:%S')

    # get_absolute_url : 객체의 상세 페이지의 주소를 반환하는 메서드.
    # 객체를 추가하거나 수정했을 때 이동할 주소를 위해 호출되기도 하고
    # 템플릿에서 상세 화면으로 이동하는 링크를 만들 때 호출하기도 함.
    # reverse : URL 패턴 이름을 가지고 해당 패턴을 찾아 주소를 만들어주는 함수.
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])