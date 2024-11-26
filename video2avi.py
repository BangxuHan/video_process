import ffmpeg
# import ffmpy
import os
import subprocess

path = '/home/kls/data/tabletennisdata/migu_new_data/Serve1/'
folder = os.listdir(path)
folder.sort()
for file in folder:
    suffix = file.split('.')[1]
    file_name = file.split('.')[0]
    print(file_name)

    if suffix == 'mp4':
        # 定义命令
        # cmd = f"ffmpeg -i \"{path + file_name}\".mp4 -c copy -map 0 -r 25 \"{path + file_name}\".avi "
        # # subprocess.run(cmd, shell=False)
        # os.system(cmd)
        os.remove(path + file_name + ".mp4")
