from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class ContactEmailTest(TestCase):
    def setUp(self):
        data = dict(
            name='Pedro Machado',
            email='pedro.machado@mail.com',
            phone='053-91234-5678',
            message='Lorem ipsum dolor sit amet',
        )
        self.response = self.client.post(r('contact'), data)
        self.email = mail.outbox[0]

    def test_email_subject(self):
        expect = 'Nova mensagem de Alex Santos'
        self.assertEqual(self.email.subject, expect)

    def test_email_sender(self):
        expect = 'alex.santos@mail.com'
        self.assertEqual(self.email.from_email, expect)

    def test_email_recipients(self):
        expect = ['contato@eventif.com.br', 'alex.santos@mail.com']
        self.assertEqual(self.email.to, expect)

    def test_email_message(self):
        contents = (
            'Alex Santos',
            'alex.santos@mail.com',
            '053-91234-5678',
            'Lorem ipsum dolor sit amet',
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)