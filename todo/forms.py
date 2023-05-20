from django import forms

from todo.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = "__all__"
