from django.urls import path
from .views import ArticleListAPIView, ArticleRetrieveAPIView


urlpatterns = [
    path('', ArticleListAPIView.as_view()),
    path('<int:pk>', ArticleRetrieveAPIView.as_view())

]
