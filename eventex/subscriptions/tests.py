from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
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
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input',6)
        self.assertContains(self.resp, 'type="text"',3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
    def test_has_form(self):
        "Context must have subscription"
        form=self.resp.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    """Testes do formulario"""
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'],list(form.fields))
    """Submissao do Formulario"""

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Victor Acioly', cpf='123123123', email='victor_acioly@hotmail.com', phone='84996530011')
        self.resp = self.client.post('/inscricao/', data)


    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEquals(302, self.resp.status_code)


    def test_send_subscribe_email(self):
        self.assertEquals(1,len(mail.outbox))

    """Se preocupando com a formatacao do txt"""
    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmacao de inscricao'

        self.assertEqual(expect,email.subject)

    """Cuidando do remetente - Depois de criar este teste eu tive que substituir a linha na views com o mesmo email que tem aqui """

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    """Cuidandno do destinatario"""

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br','victor_acioly@hotmail.com']

        self.assertEqual(expect, email.to)

    """Cuidando do corpo da mensagem"""
    def test_subscription_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Victor Acioly', email.body)
        self.assertIn('123123123', email.body)
        self.assertIn('victor_acioly@hotmail.com', email.body)
        self.assertIn('84996530011', email.body)


    """Cenario de Falha"""

class SubscribeInavlidPost(TestCase):
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
