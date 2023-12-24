```python
import os

class DocumentationGenerator:
    def __init__(self):
        self.documentation_path = None

    def create_documentation_directory(self, project_path):
        self.documentation_path = os.path.join(project_path, "documentation")
        os.makedirs(self.documentation_path, exist_ok=True)

    def generate_overview(self):
        with open(os.path.join(self.documentation_path, "overview.md"), "w") as f:
            f.write("# Project Overview\n")
            f.write("This document provides an overview of the project structure.\n")
            # More detailed overview generation can be added here

    def generate_file_structure(self, project_path):
        with open(os.path.join(self.documentation_path, "file_structure.md"), "w") as f:
            f.write("# File Structure\n")
            for root, dirs, files in os.walk(project_path):
                level = root.replace(project_path, '').count(os.sep)
                indent = ' ' * 4 * (level)
                f.write('{}{}/\n'.format(indent, os.path.basename(root)))
                subindent = ' ' * 4 * (level + 1)
                for file in files:
                    f.write('{}{}\n'.format(subindent, file))

    def generate(self, project_path):
        print("Generating project documentation...")
        self.create_documentation_directory(project_path)
        self.generate_overview()
        self.generate_file_structure(project_path)
        print("Documentation generated successfully.")
```
