from django import forms
from django.forms import fields
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:  # Form에 대한 정보
        model = Article
        # fields = '__all__'
        fields = ['title', 'content']  # 전부 다 적어주는 걸 권장함\
        # fields = ('title', 'content')
        # exclude = ('title', ) -> title 빼고 한다는 의미
        # ('title')이라고 적은 경우 -> 문자열이므로 튜플로 만들어주기 위해서는 뒤에 ,를 찍어줘야함!!
        