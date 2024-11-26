import os

path = 'Z:/pingpangclips/xigua_video/video_person_tracking/'
for i in range(155, 262):
    fold_num = str(i).zfill(6) + '/'
    folder = os.listdir(path + fold_num)
    print(fold_num[:-1], 'total file number:', len(folder))

    for i, file in enumerate(folder):
        suffix = file.split('.')[1]
        file_name = file.split('.')[0]

        if suffix == 'mp4':
            print('{}/{}'.format(i, int(len(folder)/2)), path + fold_num + file)
            os.remove(path + fold_num + file)


