from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'available', 'publication_year', 'authors', 'tags', 'cover']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'available': 'Dostępność',
            'publication_year': 'Rok publikacji',
            'authors': 'Autor',
            'tags': 'Tagi',
            'cover': 'Okładka'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'edit'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj książkę',
                'title',
                'description',
                'available',
                'publication_year',
                'authors',
                'tags',
                'cover'
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )
