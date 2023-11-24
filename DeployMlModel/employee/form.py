from django import forms
from . models import Employee

class DataForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Deparment','Eduction','Gender','Recruitment_Channel','No_of_Trainings','Age','Previous_Year_Rating',
                 'Length_Of_Service','Award_won','Average_Training_Score']
        widgets = {
            'No_of_Trainings': forms.NumberInput(attrs={'class':'form-control mt-2','placeholder': 'Enter number of trainings between 1 to 10'}),
            'Age':forms.NumberInput(attrs={'class':'form-control mt-2','placeholder': 'Enter Age between 21 to 52'}),
            'Previous_Year_Rating':forms.NumberInput(attrs={'class':'form-control mt-2','placeholder': 'Enter Rating Between 1 to 5'}),
            'Length_Of_Service':forms.NumberInput(attrs={'class':'form-control mt-2'}),
            'Award_won':forms.NumberInput(attrs={'class':'form-control mt-2','placeholder': 'Enter Winning Award Number 0 or 1'}),
            'Average_Training_Score':forms.NumberInput(attrs={'class':'form-control mt-2','placeholder': 'Enter Average Training Score Between 1 to 100'}),
        }