from django.db import models
from django import forms

# Create your models here.
YEAR = (
        ('2023', '2023'),
        ('2022', '2022'),
    )
BRANCH = (
        ('ECE', 'ECE'),
        ('CSE(select-for-similar-brances-like-csm-Ai-IT)', 'CSE(select-for-similar-brances-like-csm-Ai-IT)'),
        ('MECH','MECH'),
        ('CIVIL','CIVIL'),
        ('CHEM','CHEM'),
        ('EEE','EEE'),
    )
PACKAGE = (
    ('2-4','2-4'),
    ('4-6','4-6'),
    ('7-12','7-12'),
    ('13-18','13-18'),
    ('19-24','19-24'),
    ('more','more')
)

class Details(models.Model):
    year = models.CharField(max_length=50, choices=YEAR)
    branch = models.CharField(max_length=50, choices=BRANCH)
    placed = models.BooleanField(default=False)
    package = models.CharField(max_length=50, choices=PACKAGE, blank=True)
    

class Years(models.Model):
    year = models.CharField(max_length=50, choices=YEAR)