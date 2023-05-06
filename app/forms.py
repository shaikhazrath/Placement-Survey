from django import forms
from .models import Details, Years

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('year', 'branch', 'placed', 'package')

    def __init__(self, *args, **kwargs):
        super(DetailsForm, self).__init__(*args, **kwargs)
        # Add custom labels for fields
        self.fields['year'].label = 'Year of Passing'
        self.fields['branch'].label = 'Branch of Study'
        self.fields['placed'].label = 'Placed in Campus Recruitment?'
        self.fields['package'].label = 'Placement Package (in Lakhs per Annum)'

        # Add custom help text for fields
        self.fields['placed'].help_text = 'Select "Yes" if you were placed in a campus recruitment drive.'
        self.fields['package'].help_text = 'Enter the package you were offered in lakhs per annum, if applicable.'


class yearForm(forms.ModelForm):
    class Meta:
        model = Years
        fields = ('year',)
    
    def __init__ (self, *args, **kwargs):
        super(yearForm, self).__init__(*args, **kwargs)
        self.fields['year'].label = 'Select Year'
