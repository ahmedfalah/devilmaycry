from django.db import models
from django.core.files.base import ContentFile
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Stage1(models.Model):
    email=models.EmailField()
    Full_name=models.CharField(max_length=120,blank=True,null=True)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=20,blank=True,null=True)
    state=models.CharField(max_length=20,blank=True,null=True)
    adharnumber=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    phone_number=models.CharField(max_length=13)
    #mobile_number=models.PhoneNumberField(blank=True,null=True)
    
    def __unicode__(self):
        #return self.email
        return str(self.adharnumber)

