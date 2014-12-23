__author__ = 'student'
from django import forms
from models import Volunteer

class VolunteerForm(forms.ModelForm):
	first_name = forms.CharField(max_length=50, help_text="First Name")
	last_name = forms.CharField(max_length=50, help_text="Last Name" )
	email = forms.EmailField(max_length=100, help_text="Email")

	class Meta:
		model = Volunteer
		fields = ('first_name', 'last_name', 'email')