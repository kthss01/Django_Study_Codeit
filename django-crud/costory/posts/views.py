# from typing import List
# from django.shortcuts import redirect, render, get_object_or_404
# from django.http import Http404
from django.core.paginator import Paginator
# from django.views import View # 클래스형 뷰
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.

# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6) # 6개 포스트당 한 페이지 씩
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', {'page': page})
#     # context = {"posts" : posts}
#     # return render(request, 'posts/post_list.html', context)

class PostListView(ListView):
    model = Post
    # template_name = 'posts/post_list.html' # 기본값 모델명_list.html
    # context_object_name = 'posts' # 넘겨줄 데이터의 이름
    ordering = ['-dt_created'] # 가장 최근에 작성한 글 순
    paginate_by = 6 # 페이지네이션 몇개 단위로 할 지
    # page_kwarg = 'page' # 현재 페이지를 querystring에서 어떤 값으로 조회하는지
    

# def post_detail(request, post_id):
#     # try:
#     #     post = Post.objects.get(id=post_id)
#     # except Post.DoesNotExist:
#     #     raise Http404()
#     post = get_object_or_404(Post, id=post_id)
    
#     context = {"post": post}
#     return render(request, 'posts/post_detail.html', context)

class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post_detail.html'
    # pk_url_kwarg = 'pk' # 기본값
    # pk_url_kwarg = 'post_id'
    # context_object_name = 'post' # 모델명 소문자도 기본값

# 함수형 뷰
# def post_create(request):
#     # 유저가 form 데이터 입력하고 전송 버튼을 눌렀을 때
#     if request.method == 'POST':
#         # title = request.POST['title']
#         # content = request.POST['content']
#         # new_post = Post(
#         #     title = title,
#         #     content = content
#         # )
#         # new_post.save()
#         post_form = PostForm(request.POST)
        
#         if post_form.is_valid():
#             new_post = post_form.save() # 유효성 검증없이 넣으면 위험함
#             return redirect('post-detail', post_id=new_post.id)
#         # 데이터가 유효하지 않은 경우
#         # 중복되므로 삭제 그리고 아래 return else에서 빼버림
#         # else:
#         #     return render(request, 'posts/post_form.html', {'form': post_form})    
#     # 유저가 데이터 입력하기 전 즉 처음으로 접속하는 경우
#     else:        
#         post_form = PostForm()
    
#     return render(request, 'posts/post_form.html', {'form': post_form})

# 클래스형 뷰
# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form': post_form})
    
#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save() # 유효성 검증없이 넣으면 위험함
#             return redirect('post-detail', post_id=new_post.id)
#         return render(request, 'posts/post_form.html', {'form': post_form})

# 제네릭 뷰
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    
    def get_success_url(self):
        # return reverse('post-detail', kwargs={'post_id': self.object.id})
        return reverse('post-detail', kwargs={'pk': self.object.id})

# def post_update(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post)
        
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)
#     else: 
#         post_form = PostForm(instance=post)
        
#     return render(request, 'posts/post_form.html', {'form': post_form})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    # pk_url_kwarg = 'post_id'
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})
        # return reverse('post-detail', kwargs={'post_id': self.object.id})

# def post_delete(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', {'post': post})
    
class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html'
    # pk_url_kwarg = 'post_id'
    # context_object_name = 'post'
    
    def get_success_url(self):
        return reverse('post-list')
    
# def index(request):
#     return redirect('post-list')

class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'