from django.db import models

# Create your models here.
class Article(models.Model):
    # id = models.AutoField(primary_key=True) -> id가 1, 2, 3, 4, ... 이렇게 순서대로 자동생성 중, 이 부분이 생략되어 있음. (Model에 있는 내용이다.)

    title = models.CharField(max_length=10)  # max_length는 필수요소 -> 위젯 (클래스 변수 - 공유)
    content = models.TextField()  # max_length는 옵션
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

