from django import forms
from .models import Author
# from .models import Publisher


class BookForm(forms.Form):
    authors = Author.objects.all()
    auths = []
    for i in range(0, len(authors)):
        auths.append(str(authors[i]))
    choice = (('Author 1', auths[0]), ('Author 2', auths[1]),
              ('Author 3', auths[2]))
    bookTitle = forms.CharField(label='Book Title', max_length=100)
    bookAuthors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
