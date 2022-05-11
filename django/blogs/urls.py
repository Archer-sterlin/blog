from django.urls import path
from blogs import views


app_name = 'blogs'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list_blogs'),
    path('create/', views.CreateBlogView.as_view(), name='create_blog'),
]       
