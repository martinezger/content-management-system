from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from news_portal.models import Article, Portal, Publisher
from news_portal.views import BaseView


@login_required
def dummy(request):
    render(request, "")

class PanelView(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "news_portal/article_list.html"    
    context_object_name = "articles"


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    fields = ['short_content','title' , 'content', 'author', 'image', 'is_headline', 'image', 'date_published']
    template_name = "news_portal/article_form.html"
    success_url = reverse_lazy("panel-page")
    permission_required = ("news_portal.add_article")


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, BaseView, UpdateView):
    model = Article
    fields = ['title', 'short_content', 'content', 'author', 'image', 'is_headline', 'image', 'date_published']
    success_url = reverse_lazy('panel-page')
    permission_required = ("news_portal.change_article")
    

class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, BaseView, DeleteView):
    model = Article
    success_url = reverse_lazy('panel-page')
    permission_required = ("news_portal.delete_article")
    

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


class UserProfile(LoginRequiredMixin,UserPassesTestMixin, DetailView):

    model = Publisher
    template_name = "user_profile/user_detail.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "user_profile/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])



