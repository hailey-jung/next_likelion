from django.contrib import admin
from django.urls import path
from django.urls import reverse
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('count', views.count, name='count'),
    path('result', views.result,name='result'),
    path('info', views.info, name='info'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('update/<int:post_pk>/', views.update, name='update'),
    path('delete/<int:post_pk>/', views.delete, name='delete'),
]
