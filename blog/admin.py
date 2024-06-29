from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'image')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
