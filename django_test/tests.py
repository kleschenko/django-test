from django.test import TestCase


class HttpTest(TestCase):
    def test_context(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('settings' in response.context)
