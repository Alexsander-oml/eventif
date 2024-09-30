from django.test import TestCase

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