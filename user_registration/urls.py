
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('course/', views.CreateCourseView.as_view(), name="create_course"),
    path('class/', views.CreateClassModelView.as_view(), name="create_class"),

    path('course/<int:course_id>/', views.CourseRetrieveUpdateDeleteView.as_view(), name="course_deatils"),
    path('class/<int:class_id>/', views.ClassRetrieveUpdateDeleteView.as_view(), name="class_details"),
    
    path('create/', views.CreateUserView.as_view(), name="create_user"),
    
    path('list/', views.CreateUserView.as_view(), name="list_users"),

    path('students/', views.ListStudentsView.as_view(), name="list_students"),
    path('teachers/', views.ListTeachersView.as_view(), name="list_teachers"),

    path('students/<int:user_id>/', views.StudentsRetrieveUpdateDeleteView.as_view(), name="list_students_detail"),
    path('teachers/<int:user_id>/', views.TeachersRetrieveUpdateDeleteView.as_view(), name="list_teachers_detail"),
    
    path('login/', views.LoginView.as_view(), name='login'),
]
