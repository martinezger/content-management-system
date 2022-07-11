from django.urls import path
from news_portal.views import MainPageView, ArticleDetailView, About


urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('about/', About.as_view(), name="about"),
    path('article/<pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
