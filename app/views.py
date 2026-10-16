from django.shortcuts import render,redirect
from app.forms import employeeform
from app.models import employee
# Create your views here.
def home(request):
    employees=employee.objects.all()
    return render(request,'app/home.html',{'employees':employees})
def detail(request,id):
    emp=employee.objects.get(id=id)
    return render(request,'app/employee.html',{'employee':emp})
def add_employee(request):
    if request.method=='POST':
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form=employeeform()
    return render(request,'app/add_employee.html',{'form':form})
def success_view(request):
    return render(request,'app/success.html')