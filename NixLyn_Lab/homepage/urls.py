from django.urls import path
from .views import HomeView, ArticleDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    # Here <int:pk> is a Primary_Key value... (SQL column/row)
    # ? http://127.0.0.1:8000/article/1 
    # ! Meaning it is a potential Cyber Risk, for SQL_injections
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
]