```python
import os
import subprocess

class VersionControlIntegrator:
    def __init__(self):
        self.vcs = "git"

    def get_user_input(self):
        print("Enter the version control system you want to use (default is git):")
        vcs = input()
        if vcs:
            self.vcs = vcs

    def validate_vcs(self):
        try:
            subprocess.run([self.vcs, "--version"], check=True)
        except Exception as e:
            print(f"Invalid version control system. Using default (git). Error: {e}")
            self.vcs = "git"

    def initialize_vcs(self, project_path):
        try:
            subprocess.run([self.vcs, "init"], cwd=project_path, check=True)
            print(f"Initialized {self.vcs} repository in {project_path}")
        except Exception as e:
            print(f"Failed to initialize {self.vcs} repository. Error: {e}")

    def integrate(self, project_path):
        self.get_user_input()
        self.validate_vcs()
        self.initialize_vcs(project_path)
```
