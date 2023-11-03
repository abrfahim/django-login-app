from django import forms
from django.core import validators
# from primary_app.models import Musician, Album
from primary_app import models

class MusicianForm(forms.Form):
    class Meta:
        model = models.Musician
        fields = "__all__"