#this is the main executable, although you can use all the modules
#regardless of your needs

from module import initialize
import subprocess


class SomeDjango:

    def clear(self):
        subprocess.run(
            'clear',
            check=True
        )

    def options(self):
        return [
            'd - default',
            'u - user',
            'o - other'
        ]

    def choice(self):
        return input(':')

    def mainTemplate(self):
        opt = self.options()

        print('+----------- Lazy Django -----------+')
        for o in range(1, 7):
            if o >= 2 and o < len(opt)+2:
                print(f'| {opt[o-2]}')
            else:
                print('|')
        print('|-----------------------------------+')
        user_choice = self.choice()


def main():
    some_instance = SomeDjango()
    some_instance.mainTemplate()

if __name__ == '__main__':
    main()