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


class ProductCloth(models.Model):
    pid = models.CharField(max_length=35,null=False)
    plistedby = models.CharField(max_length=25,null=False)
    pname = models.CharField(max_length=200,null=True)
    psize = models.CharField(max_length=10,null=True)
    pcolor = models.CharField(max_length=25,null=True)
    pocasion = models.CharField(max_length=25,null=True)
    pfit = models.CharField(max_length=25,null=True)
    pfabric = models.CharField(max_length=30,null=True)
    preversible = models.CharField(max_length=5,null=True)
    pidealfor = models.CharField(max_length=15,null=True)
    pmanufacturer = models.CharField(max_length=120,null=True)
    ppacker = models.CharField(max_length=120,null=True)
    potherdetail = models.CharField(max_length=500,null=True)
    psellingprice = models.CharField(max_length=10,null=True)
    pdiscount = models.CharField(max_length=120,null=True)
    pimg1 = models.ImageField(null=True,blank=True,upload_to="products/clothes/")
    pimg2 = models.ImageField(null=True,blank=True,upload_to="products/clothes/")
    pimg3 = models.FileField(null=True,blank=True,upload_to="products/clothes/")
    pimg4 = models.FileField(null=True,blank=True,upload_to="products/clothes/")
    pimg5 = models.FileField(null=True,blank=True,upload_to="products/clothes/")
    pimg6 = models.FileField(null=True,blank=True,upload_to="products/clothes/")
    pimg7 = models.FileField(null=True,blank=True,upload_to="products/clothes/")
    pimg8 = models.FileField(null=True,blank=True,upload_to="products/clothes/")
    pactive = models.IntegerField(default=1)
    pdel = models.IntegerField(default=0)

    def __str__(self):
        return self.pid