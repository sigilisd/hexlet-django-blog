from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView

urlpatterns = [
    path("", IndexView.as_view()),
    path("<int:id>/", ArticleView.as_view(), name='article_detail'),
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsFormView.as_view()),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
]