from django.contrib import admin

# Register your models here.
from .models import *


# PhotoAdmin : 관리자 사이트에서 보이는 목록 화면을 커스터마이징할 수 있는 옵션 설정
class PhotoAdmin(admin.ModelAdmin):
    # list_display : 목록에 보일 필드를 설정. 모델의 필드를 선택하거나 별도 함수를 만들어 필드처럼 등록.
    list_display = ['id', 'author', 'created', 'updated']
    # raw_id_fields : 목록에 보일 필드를 설정. 모델의 필드를 선택하거나 별도 함수를 만들어 필드처럼 등록.
    raw_id_fields = ['author']
    # list_filter : 필터 기능을 사용할 필드를 선택. 장고가 적절하게 필터 범위를 출력
    list_filter = ['created', 'updated', 'author']
    # search_fields : 검색 기능을 통해 검색할 필드를 선택. ForeignKey 필드는 설정할 수 없음.
    search_fields = ['text', 'created']
    # ordering : 모델의 기본 정렬값이 아닌 관리자 사이트에서 기본으로 사용할 정렬값을 설정.
    ordering = ['-updated', '-created']

# Photo 모델,  PhotoAdmin 모델 등록
admin.site.register(Photo, PhotoAdmin)