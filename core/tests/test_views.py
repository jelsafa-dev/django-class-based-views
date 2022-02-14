from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.name = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.subject = 'Test subject'
        self.message = 'Test message'

        self.data_valid = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }

        self.data_invalid = {
            'name': self.name,
            'email': self.email
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data_valid)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data_invalid)
        self.assertEquals(request.status_code, 200)
