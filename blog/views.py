from django.shortcuts import render
from blog.models import BlogPost
from django.views.generic import *
# Create your views here.

class BlogPostLV(ListView):
	model = BlogPost
	template_name = 'blog/post_all.html'
	context_object_name = 'posts'
	paginate_by = 2

class BlogPostDV(DetailView):
	model = BlogPost

class BlogPostAV(ArchiveIndexView):
	model = BlogPost
	date_field = 'modify_dt'

class BlogPostYAV(YearArchiveView):
	model = BlogPost
	date_field = 'modify_dt'
	make_object_list = True

class BlogPostMAV(MonthArchiveView):
	model = BlogPost
	date_field = 'modify_dt'

class BlogPostDAV(DayArchiveView):
	model = BlogPost
	date_field = 'modify_dt'

class BlogPostTAV(TodayArchiveView):
	model = BlogPost
	date_field = 'modify_dt'