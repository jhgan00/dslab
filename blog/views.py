from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blog.models import Post
from blog.forms import *
# Create your views here.

class PostLV(ListView):
	model = Post
	template_name = 'blog/post_all.html'
	context_object_name = 'posts'
	paginate_by = 2

@method_decorator(login_required, name="post")
class PostDV(DetailView):
	model = Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CommentForm(auto_id=False)
		return context

	def post(self, request, *args, **kwargs):
		if 'comment' in self.request.POST:
			form = CommentForm(request.POST, auto_id=False)
			if form.is_valid():
				post = self.get_object()
				comment = form.save(commit=False)
				comment.post = post
				comment.save()
				return HttpResponseRedirect(reverse('blog:post_detail', args=[post.slug]))
			else:
				return render(request, self.template_name, {'form':form})

		else:
			post = self.get_object()
			post_like, post_like_created = post.like_set.get_or_create(user=request.user)
			if not post_like_created:
				post_like.delete()
			return redirect(post.get_absolute_url())

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