import os

output = '/home/kls/data/dataset1/rec_gt.txt'


def traverse_dir(path):
    with open(output, 'w') as file:
        for root, dirs, files in os.walk(path):
            # print("当前目录：", root)
            # print("子目录列表：", dirs)
            # print("文件列表：", files)
            dirs.sort()
            files.sort()
            for f in files:
                file.write(root + '/' + f + '\t' + str(f.split('_')[0]) + '\n')


dir_path = "/home/kls/data/dataset1/mls"
# print('待遍历的目录为：', dir_path)
traverse_dir(dir_path)
