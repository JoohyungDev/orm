from django.db import models
from django.contrib.auth.models import User


# 포스트를 저장할 모델 생성
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    video_file = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # <on_delete=models.CASCADE>
    # 연결된 User 객체가 삭제되면, 이 외래키를 가진 객체도 삭제
    # 사용자가 탈퇴하거나, 게시물을 삭제할 때 그 사용자의 데이터를 일괄적으로 삭제하기 위함
    # ForeignKey의 인자로 들어가는 객체가 1:N에서 1에 해당함
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title


# 댓글을 저장할 모델 추가
class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


# 태그를 저장할 모델 추가
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
