from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('predication', views.predication, name='predication'),
   
   path('emp_delete/<int:id>/',views.emp_delete,name='emp_delete'),
]
