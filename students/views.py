from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

def student_form(request):
  if request.method == 'POST' and request.FILES:
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    address=request.POST['address']
    rollno=request.POST['roll_number']
    section=request.POST['section']
    img = request.FILES['file']
    data=Student_Info(first_name=fname,last_name=lname,address=address,roll_number=rollno,section=section,image=img)
    data.save()
    messages.success(request,'Congratulations !!! Successfully Registered ')
  form=Student_Info.objects.all()
       
        
  return render(request,'form.html',{'form':form})

def homepage(request):
    return render(request, 'home.html')

def enroll(request):
   if request. method =='POST':
      fname=request.POST['firstName']
      lname=request.POST['lastName']
      address=request.POST['address']
      contact=request.POST['contact']
      message=request.POST['message']
     
      data1=Student_Query(first_name=fname,last_name=lname, address=address, contact=contact,message=message)
      data1.save()
   return render(request, 'enroll.html')

def contactUs(request):
   return render(request, 'contact.html')

def Login(request):
   return render(request, 'login.html')

def About(request):
   return render(request, 'about.html')

def Blog(request):
   return render(request, 'blog.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def show_Data(request):
   data=Student_Query.objects.all()
   print(data)
   context={'form':data}
   return render(request, 'form.html',context)

   