from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # Displays student list and adds new student
    path('<int:student_id>/', views.student_detail, name='student_detail'),  # For viewing student details
    path('<int:student_id>/edit/', views.update_student, name='update_student'),  # For editing student
    path('<int:student_id>/delete/', views.delete_student, name='delete_student'),  # For deleting student
]