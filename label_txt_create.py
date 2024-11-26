import os
import sys

root = '/home/kls/data/dataset1/mls1/'
filename = '5km/'
output = 'rec_gt_5km.txt'
filelist = os.listdir(root + filename)
filelist.sort()


with open(root + output, 'a') as file:

    for i, f in enumerate(filelist):
        file.write(filename + f + ' ' + str(f.split('_')[0]) + '\n')
