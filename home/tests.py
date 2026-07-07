from django.test import TestCase
from django.urls import reverse

from .models import Mensagem


class MensagemModelTests(TestCase):
    def test_mensagem_uses_default_author(self):
        mensagem = Mensagem.objects.create(titulo="Teste", conteudo="Texto")
        self.assertEqual(mensagem.autor, "Anônimo")


class SobrePageTests(TestCase):
    def test_sobre_page_status_code(self):
        response = self.client.get(reverse("sobre"))
        self.assertEqual(response.status_code, 200)
