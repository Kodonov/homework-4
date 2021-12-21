from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from . import models, forms
from django.views import generic

class PostListView(generic.ListView):
    template_name = 'post_list.html'
    queryset = models.Post.object.all()

    def get_queryset(self):
        return models.Post.objects.all()


class PostDetailView(generic.DetailView):
    template_name = 'post_detail.html'



class PostCreateView(generic.CreateView):
    template_name = 'add_post.html'
    form_class = forms.PostForm
    success_url = '/posts/'
    queryset = models.Post.object.all()


class PostUpdateView(generic.UpdateView):
    template_name = 'add_post.html'
    form_class = forms.PostForm
    success_url = '/posts/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PostCreateView, self).form_valid(form=form)

class PostDeleteView(generic.DeleteView):
    template_name = 'post_delete.html'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)

