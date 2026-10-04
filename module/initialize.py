from pathlib import Path
import subprocess
import shutil


class InitDjango:
    execute = subprocess
    dir_name = Path(".dependencies")

    def initializeEnvironment(self):
        self.execute.run(["python", "-m", "venv", self.dir_name])

    def deleteEnvironment(self):
        if self.dir_name.exists():
            shutil.rmtree(self.dir_name)
            print("Deleted successfully :)")
        else:
            print("Nothing to delete :D")

    def installDjango(self):
        self.execute.run(
            [self.dir_name / "bin" / "python", "-m", "pip", "install", "django"]
        )

    def checkInstallation(self):
        status = []
        if self.dir_name.exists():
            status.append("Environment deployed")

        temp = self.dir_name / "bin" / "django-admin"
        if temp.exists():
            status.append("Django installed")

        print(status)


def main():
    _init = InitDjango()
    _init.initializeEnvironment()
    _init.installDjango()
    _init.checkInstallation()
    _init.deleteEnvironment()


if __name__ == "__main__":
    main()
