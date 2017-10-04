from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')


    def test_get(self):
        """GET/ inscricao/must return status code 200"""
        response = self.client.get('/inscricao/')
        self.assertEquals(200,self.resp.status_code)

    def test_template(self):
        """Must use subscription/subscription_form.html"""

        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')


    def test_html(self):
        """Html most contain inputs tags"""

        tags = (('<form',1),
                ('<input',6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text,count in tags:
            with self.subTest():
                self.assertContains(self.resp,text, count)


    def test_csrf(self):
        """Html must contain csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        "Context must have subscription"
        form=self.resp.context['form']
        self.assertIsInstance(form,SubscriptionForm)

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Victor Acioly', cpf='123123123', email='victor_acioly@hotmail.com', phone='84996530011')
        self.resp = self.client.post('/inscricao/', data)


    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEquals(302, self.resp.status_code)


    def test_send_subscribe_email(self):
        self.assertEquals(1,len(mail.outbox))

"""Cenario de Falha"""

class SubscribePostInavlid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/',{})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEquals(200,self.resp.status_code)

    """Teste do template para fazer o template do error aparece bonitinho"""
    def test_template(self):
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    """Exibir os erros"""
    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    """Quero garantir que tenha os erros"""
    def test_has_errors(self):
        form=self.resp.context['form']
        self.assertTrue(form.errors)

"""Para mostrar uma mensagem dizendo que foi enviado"""

class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='Victor Acioly', cpf='12345678901',
                    email='victor_acioly@hotmail.com',phone='84996530011')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscricao realizada com sucesso!')
