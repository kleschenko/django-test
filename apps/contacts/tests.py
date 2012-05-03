import os
from django.test import TestCase
from django.core.urlresolvers import reverse
from contacts.models import Person
from contacts.forms import ContactsEditForm


class HttpTest(TestCase):
    def test_contacts_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('person' in response.context)
        person = response.context['person']
        self.assertTrue(person.name)

    def test_contacts_edit_get(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('contacts_edit'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_contacts_edit_post(self):
        self.client.login(username='admin', password='admin')
        person = Person.objects.get(pk=1)
        self.assertEqual(person.name, 'Kostyantyn')
        form_data = {'name': 'Test', 'surname': 'Surname',
                'birth_date': '1970-01-01',
                'bio': 'Bio', 'email': 'test@example.com'}
        response = self.client.post(reverse('contacts_edit'), form_data)
        self.assertEqual(response.status_code, 302)
        form = ContactsEditForm(form_data, instance=person)
        form.save()
        self.assertEqual(person.name, 'Test')

    def test_contacts_upload(self):
        self.client.login(username='admin', password='admin')
        image_path = 'fixtures/test_upload.jpg'
        test_upload_path = os.path.join(os.path.split(__file__)[0], image_path)
        f = open(test_upload_path, 'rb')
        post_data = {'name': 'Kostyantyn', 'surname': 'Surname',
                'birth_date': '1970-01-01', 'bio': 'Bio',
                'email': 'test@example.com', 'photo': f}
        response = self.client.post(reverse('contacts_edit'), post_data)
        self.assertEqual(response.status_code, 302)
