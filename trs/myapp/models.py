from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    userrole = models.IntegerField()

    def get_account_by_username(self, username):
        if self.username == username:
            return self

class Teacher(models.Model):
    username = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    rank = models.IntegerField()
