from django.contrib import admin
from blog.models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'modify_dt')
	list_filter = ('modify_dt',)
	search_fields = ('title', 'content')
	prepopulated_fields = {'slug':('title',)}