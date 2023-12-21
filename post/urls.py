from django.urls import path
from .views import home, blog, detail_post, dashboard


urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('dashboard/', dashboard, name='dashboard'),
    path('post/<int:post_id>/',detail_post, name='detail_post'),
]