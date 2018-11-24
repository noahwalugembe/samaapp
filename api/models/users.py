from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    user_types = (
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
        ('employee', 'Employee'),
    )
	
   
    email = models.CharField(max_length=50,null=True)
    isAdmin = models.CharField(max_length=50, choices=user_types)
    profile_picture_URL=models.CharField(max_length=200,null=True)
    #password = models.CharField(max_length=50,null=True)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name, self.email)
