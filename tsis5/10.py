import re

name = input()
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)
