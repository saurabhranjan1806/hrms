from django import forms
from .models import *


class hrmsForm(forms.ModelForm):
	class Meta:
		model = hrms
		fields = '__all__'