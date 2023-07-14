from django.shortcuts import render, HttpResponse
from myapp.models import Zone, Division, SubDivision, Consumer
from django.contrib import messages

def new(request):
    if request.method == 'POST':
        # Get the form data
        zone_id = request.POST.get('zone')
        division_id = request.POST.get('division')
        subdivision_id = request.POST.get('subdivision')
        name = request.POST.get('name')


        # Create a new consumer object
        consumer = Consumer(
            zone_id=zone_id,
            division_id=division_id,
            subdivision_id=subdivision_id,
            name=name,
            
        )
        consumer.save()

        # Display success message
        messages.success(request, "Consumer created successfully!")

    # Retrieve the available options for zones, divisions, and subdivisions
    zones = Zone.objects.all()
    divisions = Division.objects.none()
    subdivisions = SubDivision.objects.none()

    if request.method == 'GET':
        zone_id = request.GET.get('zone')
        division_id = request.GET.get('division')

        if zone_id:
            divisions = Division.objects.filter(zone_id=zone_id)

        if division_id:
            subdivisions = SubDivision.objects.filter(division_id=division_id)

    context = {
        'zones': zones,
        'divisions': divisions,
        'subdivisions': subdivisions,
    }

    return render(request, 'new.html', context)

