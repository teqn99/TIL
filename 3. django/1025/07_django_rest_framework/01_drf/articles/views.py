from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from articles.models import Article
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


# article_list에서 @api_view를 사용하는 이유는
# @api_view가 없으면, 404 페이지가 HTML로 보여짐
# @api_view가 있으면, 404 페이지가 JSON으로 응답
@api_view(['GET', 'POST'])  # DRF에서 데코레이터가 없으면 응답이 되지 않는다 -> 필수
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    # 게시글 생성
    elif request.method == 'POST':
        serializers = ArticleSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):  # 예외 발생 처리를 통해 맨아래 부분을 쓰지 않아도 됨
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)