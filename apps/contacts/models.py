from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, verbose_name='Last name')
    birth_date = models.DateField(verbose_name='Date of birth')
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=32, blank=True)
    other_contacts = models.TextField(blank=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.surname, self.name)
