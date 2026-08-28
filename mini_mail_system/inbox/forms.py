from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # sender is NOT here on purpose — the view sets it from
        # request.user, never trust a form field for "who sent this".
        fields = ['recipient', 'subject', 'body']
        # Default widget for `recipient` is a dropdown listing every
        # User row, which is fine while your user base is small. If it
        # grows, swap it for a search/autocomplete widget instead.
