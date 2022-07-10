from django.shortcuts import render
from django.views.generic import ListView
from news_portal.models import Article, Portal


class MainPageView(ListView):
    queryset = Article.objects.all()
    context_object_name = "articles"
    template_name = "news_portal/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Article.objects.filter(is_headline=True).order_by('date_updated').first()
        context['portal'] = Portal.objects.order_by('date_updated').first()
        return context
