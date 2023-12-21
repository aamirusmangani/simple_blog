from django.urls import path
from .views import home, blog, detail_post, dashboard, create_post, update_post, delete_post


urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_post/', create_post, name='create_post'),
    path('post/<int:post_id>/', detail_post, name='detail_post'),
    path('update_post/<int:post_id>/', update_post, name='update_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]