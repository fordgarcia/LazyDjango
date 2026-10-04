from pathlib import Path
import subprocess



class DefaultConfig:

    read = Path('module/default/default.txt')

    @classmethod
    def debug(cls):
        return cls.read.exists()

    @classmethod
    def ready_process(cls):
        cls.read = cls.read.read_text().split()
        cls.read.remove('start')
        cls.read.remove('end')

    @classmethod
    def read_current_default(cls):
        return cls.read

    @classmethod
    def check_current_availability(cls):
        validate = {valid:Path(valid).exists() for valid in cls.read}
        return validate

if __name__ == '__main__':
    DefaultConfig.ready_process()
    DefaultConfig.read_current_default()
    DefaultConfig.check_current_availability()
