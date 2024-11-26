from moviepy.editor import *

for i in range(1, 8):
    video_input_path = '/mnt/marathon/pingpangclips/数据集/比赛侧面素材-测试集/test/videos/test_{}.mp4'.format(i)
    video_output_path = '/home/kls/data/tabletennisdata/test_videos/test_{}.mp4'.format(i)
    # clip = VideoFileClip(video_input_path)
    # clip.write_videofile(video_output_path, fps=25)
    # clip.reader.close()
