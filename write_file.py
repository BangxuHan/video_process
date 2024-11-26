import os

path = r'/home/kls/data/TableTennisServe'
filename = 'video_material.txt'
f = os.listdir(path)
f.sort()
for i in range(len(f)):
    print(f[i])

    with open(filename, 'a') as file:
        file.write(f[i] + '\n')
