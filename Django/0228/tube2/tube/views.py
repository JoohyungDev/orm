from django.shortcuts import render
from .models import Post, Comment, Tag
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def tube_list(request):
    # 검색 q가 있을 경우 title과 content에서 해당 내용이 있는지 검색
    q = request.GET.get("q", "")
    if q:
        posts = Post.objects.filter(title__contains=q) | Post.objects.filter(
            content__contains=q
        )
        return render(request, "tube/tube_list.html", {"posts": posts, "q": q})
    posts = Post.objects.all()
    # 세번째 인자 : 템플릿에서 사용할 수 있는 context 인자.
    # posts라는 이름으로 Post.objects.all() 결과가 저장됨
    return render(request, "tube/tube_list.html", {"posts": posts})


# 특정 포스트의 세부 사항이므로 pk값을 받고 pk 값으로 필터링한 내용을 받아옴
def tube_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # 댓글을 작성하기 위한 초기 폼 객체 생성
    form = CommentForm()
    if request.method == "post":
        # 사용자의 요청을 받아 댓글 폼 객체 생성
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            # Comment(댓글) 객체를 생성하고 저장
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    return render(request, "tube/tube_detail.html", {"post": post, "form": form})


def tube_tag(request, tag):
    # tag 파라미터와 일치하는 이름을 가진 태그가 달린 모든 Post 객체를 DB에서 가져옴
    posts = Post.objects.filter(tag__name__iexact=tag)
    return render(request, "tube/tube_list.html", {"posts": posts})


@login_required
def tube_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        # author_id를 추가
        author = request.user
        post = Post.objects.create(title=title, content=content, author=author)
        post.save()
        return redirect("tube_list")
    return render(request, "tube/tube_create.html")


@login_required
def tube_update(request, pk):
    post = Post.objects.get(pk=pk)
    # 내가 쓴 게시물만 업데이트 가능
    if post.author != request.user:
        return redirect("tube_list")
    if request.method == "GET":
        return render(request, "tube/tube_update.html", {"post": post})
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        post.title = title
        post.content = content
        post.save()
    return redirect("tube_detail", pk)


@login_required
def tube_delete(request, pk):
    post = Post.objects.get(pk=pk)
    # 내가 쓴 게시물만 삭제 가능
    if post.author != request.user:
        return redirect("tube_list")
    if request.method == "POST":
        post.delete()
    return redirect("tube_list")
