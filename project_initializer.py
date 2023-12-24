```python
import os

class ProjectInitializer:
    def __init__(self):
        self.project_path = None

    def get_user_input(self):
        print("Enter the path where you want to initialize the project:")
        self.project_path = input()

    def validate_path(self):
        if not os.path.exists(self.project_path):
            print("Invalid path. Please enter a valid path.")
            return False
        return True

    def create_project_directory(self):
        project_name = input("Enter the name of your project: ")
        self.project_path = os.path.join(self.project_path, project_name)
        os.makedirs(self.project_path, exist_ok=True)

    def initialize_project(self):
        self.get_user_input()
        while not self.validate_path():
            self.get_user_input()
        self.create_project_directory()
        return self.project_path
```
