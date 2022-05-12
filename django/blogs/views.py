from django.views import generic
from django.utils import timezone


from .models import Post
from blogs.forms import CreateBlog


class BlogListView(generic.ListView):
    template_name = 'blogs/list_all_blogs.html'
    context_object_name = 'latest_blog_list'
    
    def get_queryset(self):
         return Post.objects.filter(
                date__lte=timezone.now()
                ).order_by('-date')
         
         
class CreateBlogView(generic.CreateView):
    form_class = CreateBlog
    template_name = 'blogs/create_blog.html' 