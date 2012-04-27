"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse


class HttpTest(TestCase):
    def test_logs(self):
        response = self.client.get(reverse('logs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('logs' in response.context)
        #person = response.context['person']
        #self.assertTrue(person.name)
