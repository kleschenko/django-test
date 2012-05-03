from django import forms
from django.forms.widgets import DateInput
from contacts.models import Person


class CalendarWidget(DateInput):

    def __init__(self, attrs=None, format=None):
        new_attrs = attrs or {}
        new_attrs.update({'class': 'datepicker'})
        super(CalendarWidget, self).__init__(new_attrs, format)

    class Media:
        css = {
            'all': (
                '/static/contacts/css/jquery-ui-1.8.20.custom.css',
            )
        }
        js = (
            "/static/contacts/js/jquery-1.7.2.min.js",
            "/static/contacts/js/jquery-ui-1.8.20.custom.min.js",
            "/static/contacts/js/datepicker.js",
        )


class ContactsEditForm(forms.ModelForm):
    birth_date = forms.DateField(widget=CalendarWidget())

    class Meta:
        model = Person
