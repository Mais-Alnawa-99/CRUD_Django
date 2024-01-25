
from django.shortcuts import render,redirect

from .models import Student
from .forms import Studentform



def create_student(request):
 form = Studentform() 
 if request.method == 'POST':
     form = Studentform(request.POST)
     if form.is_valid():
         try:  
             form.save()
             return redirect('student-list')
         except:
            pass
         
 else:
     form = Studentform() 
 context = {'form': form  }
 return render(request, 'create.html', context)

def student_list(request):

 students = Student.objects.all()

 context = {

 'students': students,

 }

 return render(request, 'index.html', context)

def edit_student(request, id):

 student= Student.objects.get(id=id)

 form = Studentform(instance=student)

 if request.method == 'POST':

  form = Studentform(request.POST, instance=student)
  if form.is_valid():
      try:  
           form.save()
           return redirect('student-list')
      except:
         pass
 else:
    form = Studentform(instance=student)   

 context = {'student': student,'form': form,}

 return render(request, 'edit.html', context)



def delete_student(request, id):
 student = Student.objects.get(id=id)
 if request.method == 'POST':
   student.delete()
   return redirect('student-list')
 
 else:
      student = Student.objects.get(id=id)
 context = {'student': student,}

 return render(request, 'delete.html', context)

    
