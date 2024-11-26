import os
import sys
label = 'anger', 'contempt', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise'
root = '/home/kls/data/archive_new/surprise'

filelist = os.listdir(root)
filelist.sort()
currentpath = os.getcwd()
os.chdir(root)
for i, filename in enumerate(filelist):
    os.rename(filename, 'surprise' + str(i+1).zfill(6) + '.jpg')

# for filename in filelist:
#     os.rename(filename, "wtt" + filename[3:])

os.chdir(currentpath)
sys.stdin.flush()
print('update successful')
