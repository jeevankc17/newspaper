from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin
)
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from .models import Article
from django.urls import reverse_lazy


# Create your views here.
class ArticleListView(ListView):
   model=Article
   template_name='article_list.html'
   
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
   model=Article
   template_name='article_delete.html'
   success_url=reverse_lazy('article_list')
   login_url="login"
   
   def test_func(self):
      obj = self.get_object()
      return obj.author == self.request.user
   
class ArticleDetailView(DetailView):
   model=Article
   template_name='article_detail.html'
 
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
   model=Article
   fields=('title','body')
   template_name='article_update.html'
   login_url="login"
   
   def test_func(self):
      obj = self.get_object()
      return obj.author == self.request.user
   
class ArticleCreateView(LoginRequiredMixin, CreateView):
   model=Article
   fields=('title','body')
   template_name='article_new.html'
   login_url="login"
   
   def form_valid(self, form):
      form.instance.author=self.request.user
      return super().form_valid(form)
      