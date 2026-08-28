from django.contrib import admin
from .models import Message

# Registering makes Message rows visible/editable at /admin/ — handy for
# poking at test data without writing a shell command each time.
admin.site.register(Message)
