from django.urls import path
from panel.views import PanelView, ArticleUpdateView,ArticleDeleteView, ArticleCreateView, PanelLogin, PanelLogout


urlpatterns = [
    path('', PanelView.as_view(), name='panel-page'),
    path('article/create', ArticleCreateView.as_view(), name ="article-create" ),
    path('article/<pk>/update', ArticleUpdateView.as_view(), name ="article-update" ),
    path('article/<pk>/delete', ArticleDeleteView.as_view(), name ="article-delete" ),
    path("login/", PanelLogin.as_view(), name="panel-login"),
    path("logout/", PanelLogout.as_view(), name="panel-logout"),

    ]