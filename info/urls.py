from django.contrib import admin  
from django.urls import path  
from . import views
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', views.student_list,name='student-list'),
    path('create/', views.create_student, name='create-student'),
    path('edit/<id>', views.edit_student, name='edit-student'),
    path('delete/<id>', views.delete_student, name='delete-student')
  
 
]    

