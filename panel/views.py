from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from news_portal.models import Article, Portal
from news_portal.views import BaseView


@login_required
def dummy(request):
    render(request, "")

class PanelView(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "news_portal/article_list.html"    
    context_object_name = "articles"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['short_content','title' , 'content', 'author', 'image', 'is_headline', 'image', 'date_published']
    template_name = "news_portal/article_form.html"
    success_url = reverse_lazy("panel-page")


class ArticleUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = Article
    fields = ['title', 'short_content', 'content', 'author', 'image', 'is_headline', 'image', 'date_published']
    success_url = reverse_lazy('panel-page')
    

class ArticleDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Article
    success_url = reverse_lazy('panel-page')
    

class PanelLogin(LoginView):
    template_name = 'news_portal/panel_login.html'
    next_page = reverse_lazy("panel-page")


class PanelLogout(LogoutView):
    template_name = 'news_portal/panel_logout.html'


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'news_portal/crear_cuenta_form.html'
  success_url = reverse_lazy('panel-page')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"



