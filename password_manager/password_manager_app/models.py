from django.db import models

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
