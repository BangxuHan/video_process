import cv2
import json
import os
import time


def fun2(video_path, aikf_path, result_file_name, save_path):
    # 创建视频对象

    cap = cv2.VideoCapture(video_path)
    count = 0
    # 获取视频的宽高
    video_hight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_weight = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 如果没有读取到视频地址就报错
    if not cap.isOpened():
        print("Error:", video_path)
    # 获取视频的fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(video_path)
    with open(aikf_path, "rb") as f:
        time_list = json.load(f)["AIKF"]
        for tim in time_list:
            if 'type' in tim.keys():
                # print('json文件有type键！！！！')
                if tim['type'] == 1:
                    if tim['time_out'] < 0:
                        tim["time_out"] = tim['time_in'] + 1666
                    else:
                        pass
                    print('type为1！！！')
                    start_time = tim["time_in"]
                    end_time = tim["time_out"]
                    print('start_time=====', start_time)
                    print('end_time=====', end_time)
                    start_pos = int(start_time / (1000 / fps))
                    end_pos = int(end_time / (1000 / fps))
                    cap.set(cv2.CAP_PROP_POS_FRAMES, start_pos)
                    count = start_pos
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
                    fourcc = cv2.VideoWriter_fourcc(*"XVID")
                    f_path = os.path.join(save_path, str(time.time()) + ".avi")
                    video_writer = cv2.VideoWriter(f_path, fourcc, fps, (video_weight, video_hight))
                    if start_pos > end_pos:
                        end_pos = start_pos + 75
                    while count < end_pos:
                        count += 1
                        ret, frame = cap.read()
                        video_writer.write(frame)
                    video_writer.release()
                    print(f_path)
                elif tim['type'] == 0:
                    print('type为0！！！')
                    if tim['time_out'] < 0:
                        tim["time_out"] = tim['time_in'] + 1666
                    else:
                        pass
                    start_time = tim["time_in"]
                    end_time = tim["time_out"]
                    print('start_time=====', start_time)
                    print('end_time=====', end_time)
                    start_pos = int(start_time / (1000 / fps))
                    end_pos = int(end_time / (1000 / fps))
                    cap.set(cv2.CAP_PROP_POS_FRAMES, start_pos)
                    count = start_pos
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
                    fourcc = cv2.VideoWriter_fourcc(*"XVID")
                    f_path = os.path.join(save_path, str(time.time()) + ".avi")
                    video_writer = cv2.VideoWriter(f_path, fourcc, fps, (video_weight, video_hight))
                    if start_pos > end_pos:
                        end_pos = start_pos + 75
                    while count < end_pos:
                        count += 1
                        ret, frame = cap.read()
                        video_writer.write(frame)
                    video_writer.release()
                    print(f_path)
                else:
                    continue
            else:
                count += 1
                print(count)
                print('json文件没有type键！！！！')
                if tim['time_out'] < 0:
                    tim["time_out"] = tim['time_in'] + 1666
                else:
                    pass
                start_time = tim["time_in"]
                end_time = tim["time_out"]
                print('start_time=====', start_time)
                print('end_time=====', end_time)
                start_pos = start_time / (1000 / fps)
                end_pos = end_time / (1000 / fps)
                cap.set(cv2.CAP_PROP_POS_FRAMES, start_pos)
                count = start_pos
                s_path = os.path.join(save_path, result_file_name)
                if not os.path.exists(s_path):
                    os.makedirs(s_path)
                fourcc = cv2.VideoWriter_fourcc(*"XVID")
                f_path = os.path.join(s_path, str(time.time()) + ".avi")
                video_writer = cv2.VideoWriter(f_path, fourcc, fps, (video_weight, video_hight))
                while count < end_pos:
                    count += 1
                    ret, frame = cap.read()
                    #     # cv2.imshow('fra', frame)
                    #     # cv2.waitKey(30)
                    video_writer.write(frame)
                video_writer.release()
                print(f_path)
        cap.release()


def fun(mnt_path, save_path):
    mnt_files = os.listdir(mnt_path)
    mnt_files.sort()
    count = 0
    for j in mnt_files:
        dir_Path = os.path.join(mnt_path, j)
        file2_name = os.listdir(dir_Path)
        file2_name.sort()
        for i in file2_name:
            if i[-4:] == "aiKf":
                video_path = os.path.join(dir_Path, i[:-4] + "avi")
                aikf_path = os.path.join(dir_Path, i)
                result_file_name = i[:-5]
                p2 = os.path.join(save_path, j)

                # if not os.path.exists(p2):
                fun2(video_path, aikf_path, result_file_name, p2)
                count += 1


if __name__ == '__main__':
    mnt_path = "/home/kls/data/tabletennisdata/migu"
    save_path = "/home/kls/data/tabletennisdata/migu_new_data/Hit"
    fun(mnt_path, save_path)
