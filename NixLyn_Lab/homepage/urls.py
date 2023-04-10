from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView

#urlpatterns = [
#    path("", views.homepage, name="homepage"),
#]

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    # Here <int:pk> is a Primary_Key value... (SQL column/row)
    # ! Meaning it is a potential Cyber Risk...
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),

]