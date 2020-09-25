from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')     # отображение в списке статей
    list_filter = ('status', 'created', 'publish', 'author')        # фильтарция статей по указанным полям
    search_fields = ('title', 'body')       # Строка поиска (ведет поиск по указанным полям)
    prepopulated_fields = {'slug': ('title',)}      # автоматически генерирует адр.строку (slug)
    raw_id_fields = ('author',)     # поиск по авторам
    date_hierarchy = 'publish'      # навигация по датам (по "publish")
    ordering = ('status', 'publish')        # сортировка статей по-умолчанию


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
