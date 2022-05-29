from .models import Test
from django.forms import ModelForm, TextInput

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ["fio", "group", "result"]
        widgets = {"fio": TextInput(attrs={
            'placeholder' : 'Введите фио'
        }),
            "group": TextInput(attrs={
                'placeholder': 'Введите группу'

            }),
            "result": TextInput(attrs={
                'placeholder': 'Введите значение',
                'name': 'result',
                'readonly': "readonly"

            })
        }