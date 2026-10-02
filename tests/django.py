import subprocess
from pathlib import Path

execute = subprocess
venv = Path('.dependencies')

if not venv.exists():
    execute.run(
        [
            'python',
            '-m',
            'venv',
            venv
        ]
    )

execute.run(
    [venv / 'bin' / 'django-admin']
)

# the python dir inside the dependency is needs -m for modules
# don't forget twin