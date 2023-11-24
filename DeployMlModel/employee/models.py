from django.db import models
from sklearn.ensemble import RandomForestClassifier
import joblib
from django.core.validators import MaxValueValidator, MinValueValidator


DEPARTMENT = (
                (0, 'Analytics'),
                (1, 'Finance'),
                (2, 'HR'),
                (3, 'Legal'),
                (4, 'Operations'),
                (5, 'Procurement'),
                (6, 'R&D'),
                (7, 'Sales & Marketing'),
                (8, 'Technology')
            )

EDUCTION = ((0, 'Bachelor'),
            (1, 'Below Secondary'),
            (2, 'Master & above'))

GENDER = ((0, 'Female'),
          (1, 'Male'))

RECRUITMENT_CHANNEL = ((0, 'other'),
                       (1, 'Refferd'),
                       (2, 'sourcing'))

PREDICATION = ((0, 'Not Promoted'),
               (1, 'Promoted'))

class Employee(models.Model):
    Deparment = models.PositiveIntegerField(choices=DEPARTMENT,null=True)
    Eduction = models.PositiveIntegerField(choices=EDUCTION,null=True)
    Gender = models.PositiveIntegerField(choices=GENDER,null=True)
    Recruitment_Channel = models.PositiveIntegerField(choices=RECRUITMENT_CHANNEL,null=True)
    No_of_Trainings = models.PositiveIntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(10)])
    Age = models.PositiveIntegerField(validators=[MinValueValidator(21), MaxValueValidator(52)],null=True)
    Previous_Year_Rating = models.FloatField(null=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Length_Of_Service = models.PositiveIntegerField(null=True)
    Award_won = models.PositiveIntegerField(null=True,validators=[MinValueValidator(0), MaxValueValidator(1)])
    Average_Training_Score = models.PositiveIntegerField(null=True,validators=[MinValueValidator(0), MaxValueValidator(100)])
    predication = models.PositiveIntegerField(blank=True,choices=PREDICATION)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('E:/ML model deploy with Django/DeployMlModel/model/employee model')
        self.predication = ml_model.predict([[self.Deparment,self.Eduction,self.Gender,self.Recruitment_Channel,self.No_of_Trainings,self.Age,self.Previous_Year_Rating,self.Length_Of_Service,self.Award_won,self.Average_Training_Score]])
        return super().save(*args, **kwargs)
        
    
        