from django.test import TestCase
from django.core import mail

# Create your tests here.

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao')

    def test_get(self):
        response = self.client.get('/inscricao/')
        self.assertEqual(200, response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertSequenceEqual{
            ['name', 'cpfm' , 'email', 'phone'], list(form.fields)
        }

class subscribePostTest(TestCase):
    def setUp(self):
        data = dict(name="Cleber Fonseca", cpf="0182429023", email="omelhoralek@gmail.com", phone="53-999023512")
        resp = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, resp.status_code)
    
    def test_send_subscription_email(self):
        self.assertEqual(1, len(mail.outbox))       
        
    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição!'
        self.assertEqual(expect, email.subject)
        
    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect - 'contato@eventif.com.br'
        self.assertEqual(expect, email.from_email)
        
    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventif.com.br', 'profcleberfonseca@gmail.com']
        self.assertEqual(expect, email.to)
        
    def test_subscription_email_body(self):
        email = mail.odict(name="Cleber Fonseca", cpf="0182429023", email="omelhoralek@gmail.com", phone="53-999023512")utbox[0]
        self.assertContains('Celeber Fonseca', email.body)
        self.assertContains('12345678901', email.body)
        self.assertContains('profcleberfonseca@gmail.com', email.body)
        self.assertContains('53-1234-1234', email.body)
        
class SubscribeInvalidPost(TestCase):
    def test_post(self):
        resp = self.client.post('/inscricao/', {})
        self.assertEqual(202, resp.status_code)

