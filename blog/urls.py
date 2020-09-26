from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # Обработчик приложения блога
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',       # Шаблон адреса
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),       # Шаблон для отправки почты
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag')      # Шаблон для тэгов
]