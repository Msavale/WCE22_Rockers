from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('This Is Home Page')
    return render(request, 'vesselScheduleTable.html')