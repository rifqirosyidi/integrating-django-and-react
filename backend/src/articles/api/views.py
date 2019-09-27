from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from articles.models import Article
from .serializers import ArticleSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
