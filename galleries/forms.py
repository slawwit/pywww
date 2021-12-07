from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Gallery, Photo
from django import forms


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'galleries:add_gallery'
        self.helper.add_input(Submit("submit", "Wyślij"))


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'galleries:add_photo'
        self.helper.add_input(Submit("submit", "Wyślij"))
