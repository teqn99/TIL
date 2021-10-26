from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from articles.models import Article
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from articles import serializers


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
        # raise_exception=True는 기본적으로 문제가 있을 경우 HTTP 400 코드를 응답함
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)  # 생성 성공 시 잘 만들었다는 메세지 출력
        # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # serializer = ArticleSerializer(instance=article, data=request.data)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)