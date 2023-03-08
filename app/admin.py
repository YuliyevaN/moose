from django.contrib import admin
from .models import Blog,Contact,Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_solved')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)