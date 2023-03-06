from django import forms
from .models import Bouquet


class BouquetForm(forms.ModelForm):
    class Meta:
        model = Bouquet
        fields = ('select_a_flower', 'choose_a_colour', 'arrangement',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'select_a_flower': 'Select a flower',
            'choose_a_colour': 'Choose a colour',
            'arrangement': 'Arrangement',
        }