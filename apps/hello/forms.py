#! coding: utf-8
from models import Mycard
from django import forms
from apps.hello.widgets import DatePickerWidget


class MycardForm(forms.ModelForm):
    class Meta:
        model = Mycard
        widgets = {
            'birth_date': DatePickerWidget(),
            'bio': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
            'other_contacts': forms.Textarea(attrs={'cols': 5, 'rows': 8})
        }
