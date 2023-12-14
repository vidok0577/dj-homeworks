from django.contrib import admin

from .models import Article


class


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
