from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('', views.main),
    path('recommend_vote/', views.recommend_vote),
    path('like/<int:movie_id>/', views.like_movie),
    path('recommend_personal/', views.recommend_personal),
]
