import os

import cv2


def fun2(video_path, result_file_name, save_path):
    # 创建视频对象
    cap = cv2.VideoCapture(video_path)
    # 获取视频的宽高
    video_hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_weight = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 没有读取到视频地址就报错
    if not cap.isOpened():
        print("Error:", video_path)
    print(video_path)
    # 获取视频的fps
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    if cap.isOpened():
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        i = 0
        while True:
            ret, frame = cap.read()
            if ret:
                f_path = os.path.join(save_path, result_file_name + "_" + str(i).zfill(6) + ".avi")

                if i % 16 == 0:
                    video_writer = cv2.VideoWriter(f_path, cv2.VideoWriter_fourcc(*"XVID"), fps,
                                                   (video_weight, video_hight))
                    video_writer.write(frame)
                else:
                    video_writer.write(frame)

                i += 1
            else:
                break

        video_writer.release()


def fun(mnt_path, save_path):
    mnt_files = os.listdir(mnt_path)
    mnt_files.sort()
    count = 0
    for i in mnt_files:
        video_path = os.path.join(mnt_path, i)
        result_file_name = i[:-4]

        fun2(video_path, result_file_name, save_path)
        count += 1


def read(save_path):
    save_files = os.listdir(save_path)
    save_files.sort()

    for i in save_files:
        video_path = os.path.join(save_path, i)
        cap = cv2.VideoCapture(video_path)
        # 获取视频的总帧数
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if frames != 16:
            print(i, frames)
            os.remove(video_path)
    #     else:
    #         break
    # print("no frame less than 40")


if __name__ == '__main__':
    mnt_path = "/mnt/marathon/pingpangclips/migu2022/rest/000009/"
    save_path = "/mnt/marathon/pingpangclips/migu2022/rest负样本/000009/"
    fun(mnt_path, save_path)

    read(save_path)
