from django.test import TestCase
from django.urls import reverse
from news_portal.models import Article, Publisher
from news_portal.views import MainPageView
from django.contrib.auth.models import User
from datetime import datetime
import tempfile


class TestBlog(TestCase):

    def setUp(self):
        
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name

        self.user = User.objects.create_user(username='user', email='email@example.com', password='pass')
        self.user.save()
        
        self.publisher = Publisher(user=self.user)
        self.publisher.save()
        
        self.article = Article(title="Titulo", short_content="Sub titulo", content="Cuerpo", 
                                author=self.publisher, is_headline=True,
                                image=image,
                                date_published=datetime.now())
        self.article.save()
    
        self.user_1 = User.objects.create_user(username='user_1', email='email_1@example.com', password='pass')
    
    def test_list_all_articles(self):
        response = self.client.get(reverse('main-page'))
        #Cuando se usa class based views se tiene que comparar por el nombre de instancia.
        self.assertEqual(response.resolver_match.func.view_class.__name__,  MainPageView.__name__)

