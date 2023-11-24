from django.shortcuts import render,redirect
from .form import DataForm
from . models import Employee

# Create your views here.
def index(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predication')
    else:
        form = DataForm()
    context = {
        'form' : form,
    }
    return render(request, 'index.html',context)

def predication(request):
    employee_predication = Employee.objects.all()
    context = {'employee_predication': employee_predication}
    return render(request,'predication.html',context)

def emp_delete(request,id):
    emp = Employee.objects.get(id=id)
    if emp.delete():
        return redirect('predication')
    else:
        pass
    context = {'emp':emp}
    return render(request,'predication.html',context)

def emp_update(request,id):
    pass