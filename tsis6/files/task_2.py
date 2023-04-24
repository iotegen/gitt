import os
name_file = input()

p = os.path.abspath (name_file)
print(p)
print(os.access(p, os.F_OK))
print(os.access(p, os.R_OK))
print(os.access(p, os.W_OK))
print(os.access(p, os.X_OK))