from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import *

from blog.models import Post
from blog.forms import *
# Create your views here.

class PostLV(ListView):
	model = Post
	template_name = 'blog/post_all.html'
	context_object_name = 'posts'
	paginate_by = 2

class PostDV(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CommentForm(auto_id=False)
		return context

	def post(self, request, *args, **kwargs):
		form = CommentForm(request.POST, auto_id=False)
		if form.is_valid():
			post = self.get_object()
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return HttpResponseRedirect(reverse('blog:post_detail', args=[post.slug]))
		else:
			return HttpResponseRedirect(reverse('blog:post_detail', args=[post.slug]))

class PostAV(ArchiveIndexView):
	model = Post
	date_field = 'modify_dt'

class PostYAV(YearArchiveView):
	model = Post
	date_field = 'modify_dt'
	make_object_list = True

class PostMAV(MonthArchiveView):
	model = Post
	date_field = 'modify_dt'

class PostDAV(DayArchiveView):
	model = Post
	date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
	model = Post
	date_field = 'modify_dt'

class TaggedObjectLV(ListView):
	template_name = 'blog/post_tag_list.html'
	model = Post

	def get_queryset(self):
		return Post.objects.filter(tags__name = self.kwargs.get('tag'))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tagname'] = self.kwargs['tag']
		return context