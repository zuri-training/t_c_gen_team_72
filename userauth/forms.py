import re
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ResetPassword(forms.Form):
    new_password = forms.CharField()  # TODO: add length of password
    confirm_new_password = forms.CharField()

    def clean(self):
        new_password = self.cleaned_data['new_password']
        if len(new_password) < 8:
            raise ValidationError(_('Password must be at least 8 characters'))
        if not bool(re.search(r'\d', new_password)):
            raise ValidationError(
                _('Password must contain at least one digit'))

        confirm_new_password = self.cleaned_data['confirm_new_password']

        if confirm_new_password != new_password:
            raise ValidationError(_('Passwords do not match'))

        return self.cleaned_data
