from django.shortcuts import render
from products.models import Medicine
import random

# Create your views here.

def additem(request):
    if request.method=='POST':
        a=Medicine()
        a.Mid=f'{"MED-"}{chr(random.randrange(65,90))}{chr(random.randrange(65,90))}{random.randrange(9999999999)}'
        a.Mname=request.POST['medname']
        a.Moverview=request.POST['over']
        a.Muses=request.POST['use']
        a.Mbenifits=request.POST['benifit']
        a.Msideeffects=request.POST['sideefct']
        a.Mhowtouse=request.POST['howto']
        a.Mhowdrugworks=request.POST['howdrgwrk']
        a.Msafetyadvise=request.POST['safeadv']
        a.Mmisseddose=request.POST['misseddose']
        a.Mmanufacturer=request.POST['manufac']
        a.Mexpiry=request.POST['expd']
        a.Mquicktips=request.POST['quickt']
        a.Mmakingdate=request.POST['mfd']
        a.Mmarkedprice=request.POST['markp']
        a.Mdiscount=request.POST['dis']
        mrk = int(a.Mmarkedprice)
        dis = int(a.Mdiscount)
        sp = mrk-((dis/100)*mrk)
        a.Msellingprice=sp
        a.Mimage1=request.FILES.get('img1')
        a.Mimage2=request.FILES.get('img2')
        a.Mimage3=request.FILES.get('img3')
        a.Mimage4=request.FILES.get('img4')
        a.Mimage5=request.FILES.get('img5')
        a.Mimage6=request.FILES.get('img6')
        a.save()
    return render(request,'products/addmedicine.html')


def addwatches(request):
    return render(request,'products/addwatches.html')
