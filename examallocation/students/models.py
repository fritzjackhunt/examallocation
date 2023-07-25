from django.db import models
from django.contrib.auth.models import User 
from .gender import GENDER
from .accountStatus import ACCOUNT_STATUS
from .departments import DEPARTMENTS
from .levels import LEVEL

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=16, null=True)
    regno = models.CharField(max_length=16, null=True)
    gender = models.CharField(max_length=300, null=True, choices=GENDER)
    accountStatus = models.CharField(max_length=300, null=False, choices=ACCOUNT_STATUS, default='NV') 
    dob = models.DateField(max_length=16, null=True)
    dept = models.CharField(max_length=300, null=True, choices=DEPARTMENTS)
    level = models.CharField(max_length=300, null=False, choices=LEVEL, default='100L')
    CSCT = models.CharField(max_length=15, null=False, default=0)
    CSCV = models.CharField(max_length=30, null=False, default=0)
    CSCT1 = models.CharField(max_length=15, null=False, default=0)
    CSCV1 = models.CharField(max_length=30, null=False, default=0)
    CSCT2 = models.CharField(max_length=15, null=False, default=0)
    CSCV2 = models.CharField(max_length=30, null=False, default=0)


    def __str__(self):
        if not self.user:
            return "Anonymous"
        return self.user.username


