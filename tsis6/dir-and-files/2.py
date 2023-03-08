import os
print('Exist:', os.access('C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\builtin-functions', os.F_OK))
print('Readable:', os.access('C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\builtin-functions', os.R_OK))
print('Writable:', os.access('C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\builtin-functions', os.W_OK))
print('Executable:', os.access('C:\\Users\\facto\\Desktop\\KBTU\\pp2\\pp2-23B050002\\tsis6\\builtin-functions', os.X_OK))