from django.urls import path
from . import views

urlpatterns = [
    #path('',views.PostListView.as_view(), name="blog"),
    path('', views.SearchView.as_view(), name="blog"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('create/', views.PostCreateView.as_view(), name="post_create"),
    path('edit/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),
    path('category/', views.CategoryListView, name="category_list"),
    path('category/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category/<str:cats>/', views.CategoryView, name="category"),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('<int:pk>/comment/', views.AddCommentView.as_view(), name="add_comment"),
]
