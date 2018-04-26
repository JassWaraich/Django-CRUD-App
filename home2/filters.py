
from home2.models import Availstatic
from django import forms


import django_filters

# Drop-dwon list for the analyst choices
ANALYST_CHOICES = [

('Abhishek Kumar','Abhishek Kumar'),
('Adrian Helm','Adrian Helm'),
('Alan Harris','Alan Harris'),
('Alex McKenzie','Alex McKenzie'),
('Ali Chowdhary','Ali Chowdhary'),
('Amanda Blackett','Amanda Blackett'),
('Ameekul Singh','Ameekul Singh'),
('Andres Lopez','Andres Lopez'),
('Andrew Horsford','Andrew Horsford'),
('Andrew Mark','Andrew Mark'),
('Andrew Sinker','Andrew Sinker'),
('Andrew Stewart','Andrew Stewart'),
('Arsala Shaikh','Arsala Shaikh'),
('Artur Kolpaczynski','Artur Kolpaczynski'),
]

class DateInput(forms.DateInput):
    input_type = 'date'

# function for the Django Filter 
class AvailFilter(django_filters.FilterSet):
	
	row_date =  django_filters.DateFilter(
		widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )
	analyst = django_filters.ChoiceFilter(choices=ANALYST_CHOICES)
	
	class Meta:
		model   = Availstatic
		fields  = ['row_date', 'director','manager','analyst',]

	
		


