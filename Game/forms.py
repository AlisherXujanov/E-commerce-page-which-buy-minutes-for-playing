from django import forms
from .models import Choice


class QuizForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'answer1', 'answer2',
                  'answer3', 'answer4', 'c_answer']
