from django.shortcuts import render
from .models import Medicine,ProductCloth
import random

# Create your views here.

def products(request):
    return render(request,'products/products.html')


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

def addcloths(request):
    a=ProductCloth()
    if request.method=='POST':
        a.pid = f'{"PRDCLOTH-"}{chr(random.randrange(65,90))}{chr(random.randrange(65,90))}{random.randrange(9999999999999)}'
        a.plistedby = request.user
        a.pname = request.POST.get('product')
        a.psize = request.POST.get('prsize')
        a.pcolor = request.POST.get('prcolor')
        a.pocasion = request.POST.get('whenwear')
        a.pfit = request.POST.get('prfit')
        a.pfabric = request.POST.get('prfabric')
        a.preversible = request.POST.get('prreversible')
        a.pidealfor = request.POST.get('prgender')
        a.pmanufacturer = request.POST.get('prmanufacturer')
        a.ppacker = request.POST.get('prpacker')
        a.potherdetail = request.POST.get('protherdetails')
        a.psellingprice = request.POST.get('prsellingprice')
        a.pdiscount = request.POST.get('prdiscount')
        a.pimg1 = request.FILES.get('primg1')
        a.pimg2 = request.FILES.get('primg2')
        a.pimg3 = request.FILES.get('primg3')
        a.pimg4 = request.FILES.get('primg4')
        a.pimg5 = request.FILES.get('primg5')
        a.pimg6 = request.FILES.get('primg6')
        a.pimg7 = request.FILES.get('primg7')
        a.pimg8 = request.FILES.get('primg8')
        a.save()
    return render(request,'products/addcloths.html')
