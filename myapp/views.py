from django.shortcuts import render,HttpResponse
from myapp.models import Zone, Division, SubDivision
# Create your views here.

def new(request):
    zoneid = request.GET.get('zone', None)
    divisionid = request.GET.get('division', None)
    division = None
    subdivision = None

    if zoneid:
        getzone = Zone.objects.get(id=zoneid)
        division = Division.objects.filter(zone=getzone)
    if divisionid:
        getdivision = Division.objects.get(id=divisionid)
        subdivision = SubDivision.objects.filter(division=getdivision)      
    
    zones = Zone.objects.all()

    context = {
        'zones': zones,
        'divisions': division,
        'subdivisions': subdivision,
    }

    return render(request, 'new.html', context)

