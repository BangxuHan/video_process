import os
from PIL import Image

path = '/home/kls/data/marathon/太原特殊号牌/'
folder = os.listdir(path)
folder.sort()
cnt = 0
for file in folder:
    image_path = path + file
    image = Image.open(path + file)
    image_size = image.size
    print(image_size)

    if image_size[1] < 64:
        cnt += 1
        # os.remove(image_path)
print(cnt)
