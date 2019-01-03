from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    political_party = models.CharField(max_length = 50)
    instagram_url = models.TextField(validators=[URLValidator()])
    facebook_url = models.TextField(validators=[URLValidator()])
    twitter_url = models.TextField(validators=[URLValidator()])
    whatsApp_url = models.TextField(validators=[URLValidator()])
    YouTube_url = models.TextField(validators=[URLValidator()])
    Periscope_url = models.TextField(validators=[URLValidator()])


