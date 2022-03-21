from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from .models import User  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        print("*********************************")
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = User.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = User.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = User.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = User.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  