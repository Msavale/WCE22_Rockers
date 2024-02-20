from django.shortcuts import redirect, render
from .models import Exportdocs
from django.contrib.auth.decorators import login_required
#from Login.decorators import allowed_users

# Create your views here.


#@login_required
#@allowed_users(allowed_teams=['team7'])
def blAndPhytoView(request):
    exportdocs=Exportdocs.objects.filter(blnumber=None).values('docid','invoiceno','blnumber','phytono')
    return render(request,'BLandPHYTO/blAndPhytoView.html',{'exportdocs':exportdocs})

#@login_required
#@allowed_users(allowed_teams=['team7'])
def blAndPhytoUpdate(request,docid):
    if request.method=='POST':
        if request.POST.get('phytono') and request.POST.get('phytodate'):
            Exportdocs.objects.filter(docid=docid).update(phytono=request.POST.get('phytono'),phytodate=request.POST.get('phytodate'))
        if request.POST.get('blnumber') and request.POST.get('bldate'):
            Exportdocs.objects.filter(docid=docid).update(blnumber=request.POST.get('blnumber'),bldate=request.POST.get('bldate'))
        return redirect('http://127.0.0.1:8000/blAndPhytoView/')
    else:
        exportdocs=Exportdocs.objects.filter(docid=docid).values('docid','invoiceno','blnumber','bldate','phytono','phytodate')
        return render(request,'BLandPHYTO/blAndPhytoUpdate.html',{'exportdocs':exportdocs})