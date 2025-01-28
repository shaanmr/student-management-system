from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # Student list view at the root path
    path('add/', views.student_list, name='add_student'),  # Add student (same view for creating)
    path('<int:student_id>/', views.student_detail, name='student_detail'),  # View student details
    path('<int:student_id>/edit/', views.update_student, name='update_student'),  # Edit student
    path('<int:student_id>/delete/', views.delete_student, name='delete_student'),  # Delete student
]