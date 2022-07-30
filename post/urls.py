from unicodedata import name
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
]
