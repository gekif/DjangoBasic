from django.contrib import admin

from blog.models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
