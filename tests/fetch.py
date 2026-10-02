from pathlib import Path

default = Path('../module/default/default.txt')
each_default = default.read_text().split('\n')
each_default.remove('start')
each_default.remove('end')
print(each_default)