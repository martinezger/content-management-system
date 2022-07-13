from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from news_portal.models import Article, Portal
from news_portal.views import BaseView


class PanelView(BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "news_portal/article_list.html"    
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'short_content', 'content', 'author', 'image', 'is_headline', 'image', 'date_published']
    template_name = "news_portal/article_form.html"
    success_url = reverse_lazy("panel-page")

class ArticleUpdateView(BaseView, UpdateView):
    model = Article
    fields = ['title', 'short_content', 'content', 'author', 'image', 'is_headline', 'image', 'date_published']
    success_url = reverse_lazy("panel-page")

    

class ArticleDeleteView(BaseView, DeleteView):
    model = Article
    success_url = reverse_lazy('panel-page')
    

