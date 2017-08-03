from django.forms import ModelForm
# from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _
from .models import Author, Publisher, Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'publication_date']
        label = {
            'title': _('Book Title'),
        }
        '''error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(Book)s's %(fields)s are not unique",
            }
        }'''


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state_province',
                  'country', 'website']
