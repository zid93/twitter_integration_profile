from django.db import models
import datetime
# Create your models here.

class saveToken(models.Model):
    oauth_token = models.CharField(max_length=100, null=True)
    oauth_token_secret = models.CharField(max_length=100, null=True)


class Account(models.Model):
    AccounType = [
        (0, 'Facebook'),
        (1, 'Twitter')
    ]

    username = models.CharField(max_length=100, null=True)
    id_socmed = models.CharField(max_length=100)
    account_type = models.IntegerField(choices=AccounType, default=0)
    user_parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    active = models.BooleanField(default=True)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    access_token_exp = models.DateField(null=True, blank=True, default=datetime.date.today)
    oauth_token = models.CharField(max_length=255, null=True, blank=True)
    oauth_token_secret = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.username