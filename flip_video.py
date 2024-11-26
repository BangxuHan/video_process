import ffmpeg
import os

root = '/home/kls/data/tabletennisdata/migu_new_data/Serve1'
filelist = os.listdir(root)
filelist.sort()
os.chdir(root)
for i, filename in enumerate(filelist):
    stream = ffmpeg.input(filename)
    stream = ffmpeg.hflip(stream)

    stream = ffmpeg.output(stream, 'migu' + str(i + 100539).zfill(6) + '.mp4')
    ffmpeg.run(stream)
