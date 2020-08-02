from django import forms
from .models import Content
from django.utils.text import slugify


class ContentCreateForm(forms.ModelForm):
    class Meta:
        model=Content
        fields=('title', )

    def save(self, force_insert=False, force_update=False, commit=True):
        content=super().save(commit=False)
        name=slugify(content.title)
        if commit:
            content.save()
        return content
