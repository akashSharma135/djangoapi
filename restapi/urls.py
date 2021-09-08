from django.urls import path
# from .views import article_list, article_detail
from .views import ArticleApiView, ArticleDetails

urlpatterns = [
    # path('article/', article_list, name='article_list'),
    path('article/', ArticleApiView.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view())
    # path('detail/<int:pk>/', article_detail, name='article_detail')
]