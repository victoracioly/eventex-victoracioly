from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Victor Acioly', cpf='123123123', email='victor_acioly@hotmail.com', phone='84996530011')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    """Se preocupando com a formatacao do txt"""
    def test_subscription_email_subject(self):
        expect = 'Confirmacao de inscricao'

        self.assertEqual(expect,self.email.subject)

    """Cuidando do remetente - Depois de criar este teste eu tive que substituir a linha na views com o mesmo email que tem aqui """

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    """Cuidandno do destinatario"""

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','victor_acioly@hotmail.com']

        self.assertEqual(expect, self.email.to)

    """Cuidando do corpo da mensagem"""
    def test_subscription_email_body(self):

        contents = [
            'Victor Acioly',
            '123123123',
            'victor_acioly@hotmail.com',
            '84996530011',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content,self.email.body)

