from pathlib import Path
import subprocess

execute = subprocess


environment_name = Path(".dependencies")

if not environment_name.exists():
    create_environment = ["python", "-m", "venv", ".dependencies"]
    execute.run(create_environment)

if environment_name.exists():
    execute.run([
        environment_name / 'bin' / 'python', 
        '-m',
        'pip',
        'install',
        'django'
    ])
else:
    print(environment_name.exists())
    print("failed")
