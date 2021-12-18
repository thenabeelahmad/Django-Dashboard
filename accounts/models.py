from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True,max_length=30,null=True)
    useruid = models.AutoField(primary_key=True)
    userkeyid= models.CharField(max_length=20,null=True,default="")
    userfirstname = models.CharField(max_length=30,null=True)
    useremail = models.EmailField(max_length=100,null=True)
    userphone = models.IntegerField(null=True)
    userpassword = models.CharField(max_length=12,null=True)
    userdob = models.DateField(null=True)
    useraddress = models.CharField(max_length=100,null=True)
    userpincode = models.IntegerField(null=True)
    userdeviceaddress = models.CharField(max_length=25,null=True)
    useraccountstatus = models.IntegerField(default=1)
    userdeviceaddress = models.CharField(max_length=25,null=True)
    usersystemfullinfo = models.CharField(max_length=2000,null=True,default="")
    useripaddress = models.CharField(max_length=100,null=True,default="")
    usermanufacturer = models.CharField(max_length=100,null=True)
    usermodel = models.CharField(max_length=100,null=True)
    userpcname = models.CharField(max_length=100,null=True)
    userpctype = models.CharField(max_length=100,null=True)
    userpcfamily = models.CharField(max_length=100,null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class userdevices(models.Model):
    username = models.CharField(max_length=30)
    userdeviceaddress = models.CharField(max_length=25,null=True)
    usersystemfullinfo = models.CharField(max_length=2000,null=True,default="")
    useripaddress = models.CharField(max_length=100,null=True,default="")
    usermanufacturer = models.CharField(max_length=100,null=True)
    usermodel = models.CharField(max_length=100,null=True)
    userpcname = models.CharField(max_length=100,null=True)
    userpctype = models.CharField(max_length=100,null=True)
    userpcfamily = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username

