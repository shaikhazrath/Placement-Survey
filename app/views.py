from django.shortcuts import render, redirect
from .forms import DetailsForm, yearForm
from .models import Details
from django.db.models import Count
from django.db.models import Q
import math
from collections import Counter
import json

def add_details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)

        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page
            return redirect('/')
    else:
        # Show a blank form
        form = DetailsForm()
        
    return render(request, 'index.html', {'form': form})



def chart_view(request):
    year = 2023
    if request.method == 'POST':
        selected_option = request.POST.get('Year')
        year = selected_option
        # Query data from the Details model
    details = Details.objects.all()

    # Process the data to extract the necessary information
    total_count = details.count()
    
    placed_count = details.filter(placed=True,year=year ).count()
    not_placed_count = total_count - placed_count
    
    ece_placed_count = details.filter(placed=True, year=year,branch='ECE').count()
    cse_placed_count = details.filter(placed=True,year=year, branch='CSE(select-for-similar-brances-like-csm-Ai-IT)').count()
    mech_placed_count = details.filter(placed=True,year=year, branch='MECH').count()
    civil_placed_count = details.filter(placed=True, year=year,branch='CIVIL').count()
    chem_placed_count = details.filter(placed=True, year=year,branch='CHEM').count()
    eee_placed_count = details.filter(placed=True,year=year, branch='EEE').count()
    
    # Count the occurrences of each package value
    package_counts = Counter(details.filter(placed=True,year=year).values_list('package', flat=True))
    
    # Convert the Counter object to a list of dicts for JSON serialization
    package_data = [{'label': package, 'value': count} for package, count in package_counts.items()]
    
    context = {
        'total_count': total_count,
        'placed_count': placed_count,
        'not_placed_count': not_placed_count,
        'ece_placed_count': ece_placed_count,
        'cse_placed_count': cse_placed_count,
        'mech_placed_count': mech_placed_count,
        'civil_placed_count': civil_placed_count,
        'chem_placed_count': chem_placed_count,
        'eee_placed_count': eee_placed_count,
        'package_data': json.dumps(package_data),  
        'year':year
        # Serialize the package data as JSON
    }

    # Render the chart on a webpage using Chart.js
    return render(request, 'chart.html', context)