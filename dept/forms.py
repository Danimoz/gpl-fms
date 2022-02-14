from django import forms
from django.forms import ClearableFileInput
from .models import File

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['name_of_file', 'description', 'document', 'other_docs']