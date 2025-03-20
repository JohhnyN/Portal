# filepath: d:\PROJECTS\Portal\portal\accounts\forms.py
from django import forms
from .models import Task, Comment, CustomUser


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "shared_with"]
        widgets = {
            "shared_with": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["shared_with"].queryset = self.fields[
                "shared_with"
            ].queryset.exclude(pk=user.pk)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Оставьте комментарий..."}
            ),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["custom_first_name", "custom_last_name", "surname", "photo"]
