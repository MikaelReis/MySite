<<<<<<< HEAD:blog_old/views/post_view.py
from django.views import generic

from blog_old.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
=======
from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the blog index.")
>>>>>>> a993f214c704b874056ff7b22412a018e1702d17:blog/views/post_view.py
