from django.contrib import admin

from myblog import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Article, ArticleAdmin)