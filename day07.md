



## Django REST Framework: Student Management API


### Introduction
Django REST Framework (DRF) is a robust toolkit designed for building Web APIs. This guide outlines the steps to create a simple API for managing student data, including names and roll numbers.

### Setting Up the Project
1. **Installation**: Install Django and DRF using pip.
2. **Project Creation**: Start a new Django project and create an app called `MyApp`.
3. **Configuration**: Add the app and DRF to the `INSTALLED_APPS` in the `settings.py` file.

### Creating the Student Model
Define the `Student` model in `MyApp/models.py` with fields for `name` and `rollno`. The `rollno` field is an auto-incrementing primary key.

### Database Migration
Run migration commands to apply the model changes to the database.

### Creating the Serializer
In `MyApp/serializers.py`, create a serializer for the `Student` model to convert model instances to JSON and validate incoming data.

### Creating Views
Implement CRUD operations in `MyApp/views.py` using the `APIView` class:
- **GET**: Retrieve all students or a specific student by roll number.
- **POST**: Create a new student record.
- **PUT**: Update an entire student record.
- **PATCH**: Update specific fields of a student record.
- **DELETE**: Remove a student record.

### Configuring URLs
Set up URL routing in `MyApp/urls.py` to connect API endpoints with the appropriate view methods. Update the main `urls.py` to include the app's URLs.

### Running the Server
Start the Django development server and access the API at `http://127.0.0.1:8000/student/`. You can use tools like Postman or cURL to test CRUD operations.


## Introduction
Django REST Framework (DRF) is a powerful toolkit for building Web APIs.

## Setting Up the Project
1. **Install Django and DRF**:
   ```bash
   pip install django djangorestframework
   ```

2. **Create a Django Project**:
    ```bash
    django-admin startproject My_project
    cd My_project
    ```

3. **Create an App**:
```bash
    python manage.py startapp MyApp
```
4. **Add the App and DRF to Installed Apps in settings.py**:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'students',
]

```

# Creating the Student Model
In MyApp/models.py, define the Student model:

```python
from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.AutoField(primary_key=True)
 ```

# Migrate the Database
Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```


# Creating the Serializer
Create a serializer for the Student model in MyApp/serializers.py:
```python
from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields="__all__"
```

# Creating Views
In MyApp/views.py, create views for CRUD operations:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import F, ExpressionWrapper, FloatField

from .models import Student
from .serializers import StudentSerializers



# Create your views here.
class StudentView(APIView):
    
    def get(self, request, rollno=None):
        if rollno is not None:
            try:
                student = Student.objects.get(rollno=rollno)
                serializer = StudentSerializers(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student Data not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializers(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serialize=StudentSerializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
  
        
    def put(self, request, rollno):
        try:
            student=Student.objects.get(rollno=rollno)
        except Student.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Roll NUmber is not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, rollno):
        try:
            student=Student.objects.get(rollno=rollno)
        except Student.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Roll NUmber is not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializers(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, rollno):
        try:
            student=Student.objects.get(rollno=rollno)
        except Student.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Roll NUmber is not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response({"Sucess": "Data Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

```


# Configuring URLs
In MyApp/urls.py, set up the URL routing:

```python
from django.urls import path 
from .views import StudentView 


urlpatterns = [
    path('', StudentView.as_view(),name="List_student"),
    path('<int:rollno>', StudentView.as_view()),
   
]


```

In the main urls.py file of the project (My_project/urls.py), include the student URLs:


```python

from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('MyApp.urls'))
    
]

```

# Running the Server
Run the Development Server:
```bash
python manage.py runserver

```
Access the API: You can now access the API at http://127.0.0.1:8000/students/. You can perform CRUD operations using tools like Postman or cURL.



