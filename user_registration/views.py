from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import CustomUserSerializer, ClassModelSerializer, CourseSerializer
from .models import CustomUser, Course, ClassModel

class CreateClassModelView(APIView):
    #permission_classes = [IsOwner, IsAdminUser]
    #permission_classes = [IsOwner]
    #permission_classes = [IsAdminUser]
    # permission_classes = [IsAdminUserOrIsOwner]

    def get(self, request):
        # Query for all Classes within the system
        users = ClassModel.objects.all()
        # Serialize the data
        if users:
            serializer = ClassModelSerializer(users, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data = "Errors", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        print(request.data)
        serializer = ClassModelSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateCourseView(APIView):
    def get(self, request):
        # Query for all Courses within the system
        users = Course.objects.all()
        # Serialize the data
        if users:
            serializer = CourseSerializer(users, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data = "Errors", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        print(request.data)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer  # Make sure to import your serializer
from .models import ClassModel  # Import your ClassModel model

class CreateUserView(APIView):
    def get(self, request):
        # Query for all users within the system
        users = CustomUser.objects.all()

        # Serialize the data
        if users:
            serializer = CustomUserSerializer(users, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data="Errors", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Assuming myClasses is a field in your CustomUser model
            for class_id in request.data.get('myClasses', []):
                my_class = ClassModel.objects.get(pk=class_id)
                user.myClasses.add(my_class)

            # Assuming myClasses is a field in your CustomUser model
            for course_id in request.data.get('myCourses', []):
                my_course = Course.objects.get(pk=course_id)
                user.myCourses.add(my_course)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class ListStudentsView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions

    def get(self, request):
        # Query for students with user_type="rider"
        # riders = CustomUser.objects.all()
        students = CustomUser.objects.filter(isTeacher = False)

        # Serialize the data
        if students:
            serializer = CustomUserSerializer(students, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data = "Errors", status=status.HTTP_404_NOT_FOUND)
    
class ListTeachersView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions

    def get(self, request):
        # Query for riders with user_type="rider"
        teachers = CustomUser.objects.filter(isTeacher =True)

        # Serialize the data
        if teachers:
            serializer = CustomUserSerializer(teachers, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data = "Errors", status=status.HTTP_404_NOT_FOUND)

class StudentsRetrieveUpdateDeleteView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions
    serrializer_class = CustomUserSerializer
    def get(self, request, user_id:int):

        student = CustomUser.objects.filter(isTeacher =False, pk=user_id)
        serializer = CustomUserSerializer(student, many=True)
        return Response(data=serializer.data[0], status=status.HTTP_200_OK)
       
    def put(self, request: Request, user_id:int):
        student = CustomUser.objects.filter(isTeacher = False, pk=user_id)

        serializer = self.serrializer_class(instance=student, data=request.data)

        if serializer.is_valid():
            serializer.save()
 
            response = {"message": f"Student {request.data['name']} Updated Successfully to {serializer.data['name']}", "data":serializer.data}
            return Response(data= response, status=status.HTTP_202_ACCEPTED)
        
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, user_id:int):
        student = CustomUser.objects.filter(isTeacher = False, pk=user_id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeachersRetrieveUpdateDeleteView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions
    serrializer_class = CustomUserSerializer
    def get(self, request, user_id:int):

        teacher = CustomUser.objects.filter(isTeacher = True, pk=user_id)
        serializer = CustomUserSerializer(teacher, many=True)
        return Response(data=serializer.data[0], status=status.HTTP_200_OK)
       
    def put(self, request: Request, user_id:int):
        teacher = CustomUser.objects.filter(isTeacher = True, pk=user_id)

        serializer = self.serrializer_class(instance=teacher, data=request.data)

        if serializer.is_valid():
            serializer.save()
 
            response = {"message": f"Teacher {request.data['name']} Updated Successfully to {serializer.data['name']}", "data":serializer.data}
            return Response(data= response, status=status.HTTP_202_ACCEPTED)
        
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, user_id:int):
        teacher = CustomUser.objects.filter(isTeacher = True, pk=user_id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    permission_classes = []

    def get(self, request: Request):
        content = {
            "name":str(request.user),
            "auth": str(request.auth)
            }
        return Response(data=content, status= status.HTTP_200_OK)


