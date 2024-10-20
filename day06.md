# DAY 6 : 
### Basic Notes on Django Installation and Models

#### 1. Introduction to Django
- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- It follows the Model-View-Template (MVT) architectural pattern.

#### 2. Installation

**Requirements:**
- Python (version 3.6 or later recommended)
- pip (Python package installer)

**Steps to Install Django:**
1. **Install Python:**
   - Download from the official [Python website](https://www.python.org/downloads/).
   - Ensure Python is added to your system's PATH.

2. **Install pip:**
   - Usually comes with Python. Check by running `pip --version` in the command line.

3. **Create a Virtual Environment (Optional but Recommended):**
   - Navigate to your project directory: 
     ```bash
     cd your_project_directory
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

4. **Install Django:**
   - Use pip to install Django:
     ```bash
     pip install django
     ```

5. **Verify Installation:**
   - Check the installed Django version:
     ```bash
     python -m django --version
     ```

#### 3. Creating a New Django Project
1. **Start a Project:**
   ```bash
   django-admin startproject project_name
   ```
2. **Navigate into the Project Directory:**
   ```bash
   cd project_name
   ```

3. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   - Access the development server at `http://127.0.0.1:8000/`.

#### 4. Creating Models in Django

**What are Models?**
- Models are Python classes that define the structure of your database. They represent the data you want to store.

**Steps to Create Models:**
1. **Create an App:**
   ```bash
   python manage.py startapp app_name
   ```

2. **Define Models:**
   - Open `models.py` in your app directory and define your model classes.
   ```python
   from django.db import models

   class MyModel(models.Model):
       field_name = models.CharField(max_length=100)
       another_field = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
   ```

3. **Register the App:**
   - Add the app to `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'app_name',
   ]
   ```

4. **Create and Apply Migrations:**
   - Create migrations for your model:
   ```bash
   python manage.py makemigrations
   ```
   - Apply migrations to the database:
   ```bash
   python manage.py migrate
   ```

5. **Using the Django Admin:**
   - Register your model in `admin.py` to manage it through the Django admin interface:
   ```python
   from django.contrib import admin
   from .models import MyModel

   admin.site.register(MyModel)
   ```

6. **Create a Superuser:**
   - Run the following command to create an admin user:
   ```bash
   python manage.py createsuperuser
   ```
   - Access the admin interface at `http://127.0.0.1:8000/admin/`.

#### 5. Conclusion
- Django simplifies web development and provides robust features for managing databases through models.
- Understanding installation and model creation is essential for building Django applications.

#### 6. Additional Resources
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) 

# Models
### Detailed Overview of Django Models

#### 1. Introduction to Django Models
Django models serve as the backbone of your application's data structure. They define the fields and behaviors of the data you’re storing, mapping Python classes to database tables.

#### 2. Creating a Model

**Basic Structure:**
```python
from django.db import models

class MyModel(models.Model):
    # Define fields
    field_name = models.FieldType(options)
```

#### 3. Common Field Types

Here’s a detailed list of commonly used field types in Django models:

- **CharField**
  - Stores short text strings.
  - Required parameters:
    - `max_length`: Maximum length of the string.
  - Example:
    ```python
    name = models.CharField(max_length=100)
    ```

- **TextField**
  - Stores large text strings without a maximum length.
  - Example:
    ```python
    description = models.TextField()
    ```

- **IntegerField**
  - Stores integer values.
  - Example:
    ```python
    age = models.IntegerField()
    ```

- **FloatField**
  - Stores floating-point numbers.
  - Example:
    ```python
    price = models.FloatField()
    ```

- **BooleanField**
  - Stores `True` or `False` values.
  - Example:
    ```python
    is_active = models.BooleanField(default=True)
    ```

- **DateField**
  - Stores date values (year, month, day).
  - Example:
    ```python
    birth_date = models.DateField()
    ```

- **DateTimeField**
  - Stores date and time values.
  - Options:
    - `auto_now`: Sets the field to the current date/time every time the object is saved.
    - `auto_now_add`: Sets the field to the current date/time when the object is created.
  - Example:
    ```python
    created_at = models.DateTimeField(auto_now_add=True)
    ```

- **EmailField**
  - Stores email addresses.
  - Example:
    ```python
    email = models.EmailField()
    ```

- **URLField**
  - Stores URLs.
  - Example:
    ```python
    website = models.URLField()
    ```

- **ImageField**
  - Stores images and requires the Pillow library.
  - Example:
    ```python
    profile_picture = models.ImageField(upload_to='profiles/')
    ```

- **ForeignKey**
  - Defines a many-to-one relationship.
  - Required parameters:
    - `to`: The model that is being referenced.
    - `on_delete`: Defines the behavior when the referenced object is deleted.
  - Example:
    ```python
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```

- **ManyToManyField**
  - Defines a many-to-many relationship.
  - Example:
    ```python
    groups = models.ManyToManyField(Group)
    ```

- **OneToOneField**
  - Defines a one-to-one relationship.
  - Example:
    ```python
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    ```

#### 4. Field Options
Each field can have several options to customize its behavior:

- **null**: If set to `True`, allows `NULL` values in the database.
- **blank**: If set to `True`, allows the field to be empty in forms.
- **default**: Sets a default value for the field.
- **unique**: Ensures all values in this field are unique across the table.
- **choices**: Limits the values of a field to a specific set of choices.
  ```python
  STATUS_CHOICES = [
      ('draft', 'Draft'),
      ('published', 'Published'),
  ]
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)
  ```

#### 5. Custom Methods
You can define methods within your model class to add custom logic. A common practice is to define a `__str__` method to return a human-readable string representation of the model instance.

Example:
```python
class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

#### 6. Creating and Applying Migrations
Migrations are Django’s way of propagating changes you make to your models into the database schema.

1. **Create Migrations:**
   - After defining or modifying models:
   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations:**
   - To update the database:
   ```bash
   python manage.py migrate
   ```

#### 7. Using Models in Views
You can interact with your models in views to create, retrieve, update, and delete records.

**Example of Creating and Retrieving Records:**
```python
from .models import MyModel

# Create a new entry
new_entry = MyModel(name="John Doe")
new_entry.save()

# Query all entries
all_entries = MyModel.objects.all()

# Filter entries
filtered_entries = MyModel.objects.filter(name="John Doe")

# Update an entry
entry = MyModel.objects.get(id=1)
entry.name = "Jane Doe"
entry.save()

# Delete an entry
entry.delete()
```

#### 8. Admin Interface
To manage models through the Django admin interface:

1. **Register your model in `admin.py`:**
   ```python
   from django.contrib import admin
   from .models import MyModel

   admin.site.register(MyModel)
   ```

2. **Access the admin panel:**
   - Navigate to `http://127.0.0.1:8000/admin/`.




#### 11. Additional Resources
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django QuerySet Documentation](https://docs.djangoproject.com/en/stable/topics/db/queries/)


## Problem: JUMP GAME

The function `jump` is designed to determine the number of jumps needed to reach the last index of a list, where each element specifies the maximum jump length from that position. It starts from the second element (index 1) and counts the jumps taken while moving through the list. The function checks whether a jump would exceed the bounds of the list or if a zero is encountered, which would indicate that no further jumps are possible. In such cases, it returns `False`. If the function successfully reaches the last index, it returns the total number of jumps made. If reaching the end is not feasible, it outputs a message stating that the jump is not possible; otherwise, it displays the total number of jumps taken.

```python
def jump(l):
    # Start from the second element (index 1)
    i=1  
    # Initialize the count of jumps
    count=1 
    # Continue until the index exceeds the length of the list 
    while i<len(l):  
        #print(l[i])  # Uncomment to see the current jump value
        # Check if the jump exceeds the bounds of the list
        if i+l[i]>len(l): 
            # Return False if jump is not possible 
            return False  
        # If the current jump value is 0, can't proceed
        elif l[i]==0:  
            # Return False if jump is not possible
            return False  
        # Move to the next index based on the jump value
        i+=l[i]  
        # Increment the count of jumps
        count+=1  
        # Check if we have reached the last index
        if i==len(l)-1:  
             # Return the total number of jumps
            return count 
# Example list of jump values
l1=[2,0,1,0,4]  
# Call the jump function with the list
op=jump(l1)  
# Check if the jump was successful
if op==False:  
     # Output if jump isn't possible
    print(f"The jump is not possible") 
else:
     # Output the number of jumps
    print(f"The jump steps are {op}") 
```