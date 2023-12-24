```python
import os

class TemplateManager:
    def __init__(self):
        self.templates = {
            "web_development": "path_to_web_dev_template",
            "data_science": "path_to_data_science_template",
            # Add more templates as needed
        }

    def get_user_input(self):
        print("Enter the type of your project:")
        print("Options: " + ", ".join(self.templates.keys()))
        project_type = input()
        while project_type not in self.templates:
            print("Invalid project type. Please enter a valid project type.")
            project_type = input()
        return project_type

    def apply_template(self, project_path):
        project_type = self.get_user_input()
        template_path = self.templates[project_type]
        self.copy_template(template_path, project_path)

    def copy_template(self, template_path, project_path):
        # This is a placeholder for the actual implementation
        # The actual implementation should copy the directory structure and files from the template_path to the project_path
        print(f"Copying template from {template_path} to {project_path}")
```
