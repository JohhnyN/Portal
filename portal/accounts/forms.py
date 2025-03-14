# filepath: d:\PROJECTS\Portal\portal\accounts\forms.py
from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "shared_with", "is_completed"]
        widgets = {
            "shared_with": forms.CheckboxSelectMultiple,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Оставьте комментарий..."}
            ),
        }
