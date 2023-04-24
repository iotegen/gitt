import os
path = input()

all = os.listdir()
result =[]
resfile = []
resdir = []
for(dir_path, dir_names , file_names) in os.walk(path):
    result.extend(dir_path.split())
    resfile.extend(file_names)
    resdir.extend(dir_names)

print(result)
print(all)
print(resfile)
print(resdir)