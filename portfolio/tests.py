from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            titulo="Meu Post de Teste",
            conteudo="Conteúdo de teste para a EBAC."
        )

    def test_post_criacao(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), "Meu Post de Teste")

