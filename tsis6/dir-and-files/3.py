import os
print("Test a path exists or not:")
path = r'text.txt'
print(os.path.exists(path))
path = r'C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis6\builtin-functions'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))