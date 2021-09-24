from posts.forms import PostForm
from django.shortcuts import redirect, render, get_object_or_404
# from django.http import Http404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6) # 6개 포스트당 한 페이지 씩
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    return render(request, 'posts/post_list.html', {'page': page})
    # context = {"posts" : posts}
    # return render(request, 'posts/post_list.html', context)

def post_detail(request, post_id):
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist:
    #     raise Http404()
    post = get_object_or_404(Post, id=post_id)
    
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)

def post_create(request):
    # 유저가 form 데이터 입력하고 전송 버튼을 눌렀을 때
    if request.method == 'POST':
        # title = request.POST['title']
        # content = request.POST['content']
        # new_post = Post(
        #     title = title,
        #     content = content
        # )
        # new_post.save()
        post_form = PostForm(request.POST)
        
        if post_form.is_valid():
            new_post = post_form.save() # 유효성 검증없이 넣으면 위험함
            return redirect('post-detail', post_id=new_post.id)
        # 데이터가 유효하지 않은 경우
        # 중복되므로 삭제 그리고 아래 return else에서 빼버림
        # else:
        #     return render(request, 'posts/post_form.html', {'form': post_form})    
    # 유저가 데이터 입력하기 전 즉 처음으로 접속하는 경우
    else:        
        post_form = PostForm()
    
    return render(request, 'posts/post_form.html', {'form': post_form})

def post_update(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post.id)
    else: 
        post_form = PostForm(instance=post)
        
    return render(request, 'posts/post_form.html', {'form': post_form})

def post_delete(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post': post})
    
def index(request):
    return redirect('post-list')