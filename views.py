from django.shortcuts import redirect, render
from .models import Exportdocs
from django.contrib.auth.decorators import login_required
#from Login.decorators import allowed_users

# Create your views here.


#@login_required
#@allowed_users(allowed_teams=['team10'])
def egmView(request):
    #Static input values are taken
    exportdocs=Exportdocs.objects.filter(egmno='123').values('docid','invoiceno','shippingbillnumber','shippingbilldate')
    return render(request,'EGM_Status/egmView.html',{'exportdocs':exportdocs})

#@login_required
#@allowed_users(allowed_teams=['team10'])
def egmUpdate(request,docid):
    if request.method=='POST' and request.POST.get('egmno') and request.POST.get('egmdate'):
        Exportdocs.objects.filter(docid=docid).update(egmno=request.POST.get('egmno'),egmdate=request.POST.get('egmdate'))
        # Local machine url provided
        return redirect('http://127.0.0.1:8000/egmView/')
    else:
        exportdoc=Exportdocs.objects.filter(docid=docid).values('docid','invoiceno','shippingbillnumber','shippingbilldate')
        return render(request,'EGM_Status/egmUpdate.html',{'exportdoc':exportdoc})

def egmInfo(request,docid):
    if request.method=='POST' and request.POST.get('egmno') and request.POST.get('egmdate'):
        Exportdocs.objects.filter(docid=docid).update(egmno=request.POST.get('egmno'),egmdate=request.POST.get('egmdate'))
        # Local machine url provided
        return redirect('http://127.0.0.1:8000/egmView/')
    else:
        exportdocs=Exportdocs.objects.filter(docid=docid).values('docid','invoiceno','shippingbillnumber','shippingbilldate','egmno','egmdate')
        return render(request,'EGM_Status/egmInfo.html',{'exportdocs':exportdocs})