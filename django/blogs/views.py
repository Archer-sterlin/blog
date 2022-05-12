from django.views import generic
from django.utils import timezone

from .models import Category, Post
from blogs.forms import CreateBlog

import datetime
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

# from blogs.forms import CreateBlog, CustomUserCreationForm
# from blogs.mixins import LoginRequiredMixin



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
    
    
class DetailView(generic.DetailView):
    template_name = 'blogs/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(date__lte=timezone.now())
 
class DashboardView(generic.TemplateView):
    template_name = 'blogs/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        user = self.request.user
        
        # How many blogs we have in total
        posts = Post.objects.filter(author__id=user.id)
        
        # How many new blogs in the last 30 days
        thirty_days_ago = datetime.date.today() - datetime.timedelta(days=30)

        total_in_past30 = Post.objects.filter(
            author__id=user.id,
            date__gte=thirty_days_ago
        ).count()

        context.update({
            "total_blogs_count": posts.count(),
            "total_in_past30": total_in_past30,
            "blogs": posts
        })
        return context
    

class CreateBlogView(generic.CreateView):
    form_class = CreateBlog
    template_name = 'blogs/create_blog.html' 
    
    
class UpdateBlogView(generic.UpdateView):
    model = Post
    template_name = 'blogs/update_blog.html'
    fields = ['title', 'body', 'image'] 
    

class DeleteBlog(generic.DeleteView):
    model = Post
    template_name = 'blogs/delete_blog.html'
    success_url = reverse_lazy('blogs:list_blogs')  