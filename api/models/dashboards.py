from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


#from api.models.users import User


class Dashboard(TimeStampedModel):
    community_unit= models.CharField(max_length=50, null=True)	
    school_id= models.CharField(max_length=50, null=True)
    name= models.CharField(max_length=100, null=True)
    olevel_students	 = models.CharField(max_length=50,null=True)
    alevel_students	 = models.CharField(max_length=50,null=True)
    boarding_students = models.CharField(max_length=50,null=True)
    day_students	 = models.CharField(max_length=50,null=True)
    boarding_fee_S3	= models.CharField(max_length=50,null=True)
    day_fee_S3	= models.CharField(max_length=50,null=True)
    boarding_fee_S5	= models.CharField(max_length=50,null=True)
    day_fee_S5	= models.CharField(max_length=50,null=True)
    female_students	= models.CharField(max_length=50,null=True)
    male_students= models.CharField(max_length=50,null=True)	
    number_of_students	= models.CharField(max_length=50,null=True)
    number_of_teachers= models.IntegerField(max_length=50,null=True)	
    location= models.CharField(max_length=50, null=True)	
    date_school_enrolled= models.DateField(null=True)