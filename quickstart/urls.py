from django.urls import path
from quickstart import views

urlpatterns = [
    path('Article/', views.makearticle_list),
    path('Article/<int:pk>/', views.article_detail),
    
]