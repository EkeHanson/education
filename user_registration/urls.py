
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('course/', views.CreateCourseView.as_view(), name="create_course"),
    path('class/', views.CreateClassModelView.as_view(), name="create_class"),

    path('course/<int:course_id>/', views.CourseRetrieveUpdateDeleteView.as_view(), name="course_deatils"),
    path('class/<int:class_id>/', views.ClassRetrieveUpdateDeleteView.as_view(), name="class_details"),


    path('message/', views.CreateMessageView.as_view(), name="create_message"),
    path('message/<int:message_id>/', views.MessageRetrieveUpdateDeleteView.as_view(), name="message_details"),
    
    path('create/', views.CreateUserView.as_view(), name="create_user"),

    path('students/', views.ListStudentsView.as_view(), name="list_students"),
    path('teachers/', views.ListTeachersView.as_view(), name="list_teachers"),

    path('login/', views.LoginView.as_view(), name='login'),
]
