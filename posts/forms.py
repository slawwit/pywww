from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from tags.models import Tag
from .models import Post
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from dal import autocomplete


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image', 'tags']
        labels = {
            "title": "Tytuł",
            "content": "Treść",
            "published": "Opublikowany",
            "sponsored": "Sponsorowany",
            "image": "Obrazek"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'add'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj post',
                'title',
                'content',
                'published',
                'sponsored',
                'image',
                'tags'
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )
