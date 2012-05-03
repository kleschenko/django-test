from django import forms
from django.forms.widgets import DateInput
from contacts.models import Person

attrs_right = {'class': 'right'}


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
    birth_date = forms.DateField(widget=CalendarWidget(),
            label='Date of birth')

    class Meta:
        model = Person
        widgets = {
                'email': forms.TextInput(attrs=attrs_right),
                'jabber': forms.TextInput(attrs=attrs_right),
                'skype': forms.TextInput(attrs=attrs_right),
                'other_contacts': forms.Textarea(attrs=attrs_right),
                'bio': forms.Textarea(attrs=attrs_right),
        }
        fields = ('name', 'surname', 'birth_date', 'photo', 'email',
                'jabber', 'skype', 'other_contacts', 'bio')
