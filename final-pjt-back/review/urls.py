from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path('', views.review_list),
    path('<int:movie_id>/', views.review_detail_create),
    path('<int:movie_id>/<int:review_id>/', views.review_update_delete),
    path('comment/<int:review_id>/', views.comment_list_create),
    path('comment/<int:review_id>/<int:comment_id>/', views.comment_update_delete),
]
