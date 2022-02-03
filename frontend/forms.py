from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'id_socmed', 'user_parent', 'account_type', 'access_token', 'access_token_exp',
                  'oauth_token', 'oauth_token_secret',)