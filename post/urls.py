from django.urls import path
from .views import home, blog, detail_post, dashboard, create_post


urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_post/', create_post, name='create_post'),
    path('post/<int:post_id>/',detail_post, name='detail_post'),
]