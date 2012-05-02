"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse


class HttpTest(TestCase):
    def test_contacts_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('person' in response.context)
        person = response.context['person']
        self.assertTrue(person.name)

    def test_contacts_edit(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('contacts_edit'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
