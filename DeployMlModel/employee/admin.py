from django.contrib import admin
from .models import Employee
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('Deparment', 'Eduction', 'Gender', 'Recruitment_Channel','No_of_Trainings','Age','Previous_Year_Rating','Length_Of_Service',
                    'Award_won','Average_Training_Score','predication')
admin.site.register(Employee, DataAdmin)