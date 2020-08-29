from django import forms
from .models import Poll, Choice

# BROWSER_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'


class PollForm(forms.ModelForm):
    # created_at = forms.DateTimeField(required=False, label='Создания опроса',
    #                                  input_formats=[BROWSER_DATETIME_FORMAT,
    #                                                 '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
    #                                                 '%Y-%m-%d %H:%M:%S'])
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['variant']