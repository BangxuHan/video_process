import os
import shutil

src_path = '/home/kls/data/marathon/27781/1111111/'

for i in range(16, 70):
    folder = os.listdir(src_path)
    print(len(folder))
    folder.sort()

    # print(i)
    new_path = '/home/kls/data/marathon/27781/{}/'.format(i)
    n = 0
    for files in folder:
        if n < 1000:
            print(files)
            shutil.move(src_path + files, new_path + files)  # 移动文件
        n += 1

# path = '/home/kls/data/marathon/27781/'
# for i in range(1, 70):
#     # if not os.path.exists(path + str(i)):
#     #     os.makedirs(path + str(i))
#     if len(os.listdir(path + str(i))) < 1000 and i != 1:
#         print(i)
