from django.db import models

# Create your models here.
class Medicine(models.Model):
    Mid = models.CharField(max_length=16,null=True)
    Mname = models.CharField(max_length=400,null=True)
    Moverview = models.CharField(max_length=400,null=True)
    Muses = models.CharField(max_length=800,null=True)
    Mbenifits =models.CharField(max_length=800,null=True)
    Msideeffects =models.CharField(max_length=800,null=True)
    Mhowtouse =models.CharField(max_length=800,null=True)
    Mhowdrugworks =models.CharField(max_length=800,null=True)
    Msafetyadvise =models.CharField(max_length=800,null=True)
    Mmisseddose =models.CharField(max_length=1000,null=True)
    Mquicktips =models.CharField(max_length=1500,null=True)
    Mmanufacturer =models.CharField(max_length=100,null=True)
    Mexpiry =models.DateField(null=True)
    Mmakingdate =models.DateField(null=True)
    Mmarkedprice = models.IntegerField(null=True)
    Mdiscount = models.IntegerField(null=True)
    Msellingprice = models.IntegerField(null=True)
    Mimage1 = models.FileField(null=True)
    Mimage2 = models.FileField(null=True)
    Mimage3 = models.FileField(null=True)
    Mimage4 = models.FileField(null=True)
    Mimage5 = models.FileField(null=True)
    Mimage6 = models.FileField(null=True)


    def __str__(self):
        return self.Mname
