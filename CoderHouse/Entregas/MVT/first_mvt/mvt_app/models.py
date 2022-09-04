from django.db import models

# FammilyTree
"""
class Grandparents(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)
    age = models.IntegerField()

class Parents(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)
    age = models.IntegerField()


class Brothers(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)
    age = models.IntegerField()
"""

class Familiares(models.Model):
    name = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)
    relationship = models.CharField(max_length=128)
    age = models.IntegerField()

