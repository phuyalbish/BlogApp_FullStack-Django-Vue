from django.urls import  path
from article import views



urlpatterns = [

    path('getArticle/<int:id>', views.getArticle),
    path('getAllArticle/', views.getAllArticle),
    path('editArticle/<int:id>', views.editArticle,),
    path('deleteArticle/<int:id>', views.deleteArticle),
    path('addArticle/', views.addArticle),
]