from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Submit, Button

from .models import Country


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country

        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'country-form'
        self.helper.form_class = 'blue'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout('name')
        # self.helper.layout.append(
        #     HTML("""<button>A</button>"""),
        # )

        self.helper.add_input(Submit('submit-name', 'Save'))
        self.helper.layout.append(HTML(
            """<a class="btn btn-default" href="{% url "country-list" %}">Cancel</a>""")),
        # self.helper.add_input(Button('delete', 'Delete', onclick='window.location.href="{}"'.format('delete')))

    def clean_name(self):
        data = self.cleaned_data['name']

        if data == "Alemania":
            raise ValidationError(
                "That name is forbidden.", code="invalid-name")

        return data
