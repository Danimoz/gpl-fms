from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dept.models import Dept

class StaffUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    department = forms.ModelChoiceField(queryset=Dept.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'department']
        help_texts = {
            "username": None,
        }

    def __init__(self, *args, **kwargs):
        super(StaffUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

