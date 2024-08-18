from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForms
from .models import *
from .filters import PostFilter
import datetime



class PostsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostsSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'post_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForms
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/post/articles/create':
            post.state_news = 'ST'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForms
    model = Post
    template_name = 'post_edit.html'

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     if self.request.path == '/post/articles/update':



class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
