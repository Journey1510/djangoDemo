from django.contrib import admin

from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']


admin.site.register(Blog, BlogAdmin)
