from django import forms


class BookForm(forms.Form):
    bookTitle = forms.CharField(label='Book Title', max_length=100)
