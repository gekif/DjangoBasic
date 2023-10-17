from django.contrib import admin

from blog.models import Post, Comment


# Register your models here.
class PostAmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'content']


admin.site.register(Post, PostAmin)
admin.site.register(Comment, PostAmin)
