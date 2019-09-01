from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import Photo

# 사진 목록 뷰
@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

# 사진 업로드 뷰
class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'     # 실제 사용할 템플릿 설정

    # form_valid : 업로드를 끝낸 후 이동할 페이지를 호출하기 위해 사용하는 메서드
    # 이 메서드를 오버라이드해서 작성자를 설정하는 기능을 추가
    def form_valid(self, form):
        # 작성자 : 현재 로그인한 사용자
        form.instance.author_id = self.request.user.id
        # 입력값 검증
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

# 사진 삭제 뷰
class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

# 사진 수정 뷰
class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'