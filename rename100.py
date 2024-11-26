import os
import sys

root = '/home/kls/data/marathon/太原特殊号牌'

filelist = os.listdir(root)
filelist.sort()
currentpath = os.getcwd()
os.chdir(root)
for i, filename in enumerate(filelist):
    os.rename(filename, str(filename.split('_')[0]) + '_' + str(i+1).zfill(4) + '.jpg')

# for filename in filelist:
#     os.rename(filename, "wtt" + filename[3:])

os.chdir(currentpath)
sys.stdin.flush()
print('update successful')
