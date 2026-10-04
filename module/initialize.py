from pathlib import Path
import subprocess
import shutil
from . import default


class InitDjango:
    execute = subprocess
    dir_name = Path(".dependencies")

    def _initializeEnvironment(self):
        self.execute.run(["python", "-m", "venv", self.dir_name])

    def _deleteEnvironment(self):
        if self.dir_name.exists():
            shutil.rmtree(self.dir_name)
            print("Deleted successfully :)")
        else:
            print("Nothing to delete :D")

    def _deleteProject(self, name:Path):
        if name.exists():
            shutil.rmtree(name)
            print('Deleted Successfully :)')
        else:
            print('Nothing to delete :)')

    def _delete_both(self, name):
        self._deleteEnvironment()
        self._deleteProject(name)

    def _installDjango(self):
        self.execute.run(
            [self.dir_name / "bin" / "python", "-m", "pip", "install", "django"]
        )

    def _make_django_project(self, name="project") -> bool:
        check = self.dir_name / 'bin' / 'django-admin'

        print(check.exists())
        if check.exists():
 
            create_project = [
                str(check),
                'startproject',
                name
            ]

            self.execute.run(
                create_project                
            )

            return True
        return False

    def _checkInstallation(self):
        status = []
        if self.dir_name.exists():
            status.append("Environment deployed")

        temp = self.dir_name / "bin" / "django-admin"
        if temp.exists():
            status.append("Django installed")

        return len(status) == 2

    # main functions
    def make_default(self):
        self._initializeEnvironment()
        self._installDjango()
        project_status = self._make_django_project()
        if default.DefaultConfig.debug() and self._checkInstallation() and project_status:
            default.DefaultConfig.ready_process()
            default_path = [
                Path("project") / url
                for url in default.DefaultConfig.check_current_availability().keys()
            ]

            for individual_path in default_path:
                individual_path.mkdir(parents=True)
        # self._deleteEnvironment()


def main():
    temp = InitDjango()
    temp.make_default()
    #temp._delete_both(Path('project'))


if __name__ == "__main__":
    main()
