from django.contrib import admin
from .models import Post, Comment, Category


# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine, ]
    list_display = ('id', 'title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)