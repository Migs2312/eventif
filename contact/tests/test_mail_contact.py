from django.test import TestCase
from django.core import mail

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Miguel Martins",
                    email='andrademartins.m@gmail.com', phone='53-12345-6789', message="Olá, mundo")
        self.client.post('/contact/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Novo contato.'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'andrademartins.m@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'Miguel Martins', 'andrademartins.m@gmail.com', '53-12345-6789', 'Olá, mundo'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)