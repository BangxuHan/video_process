import os
import shutil
from glob import glob


def mymovefile(srcfile, dstpath):
    fpath, fname = os.path.split(srcfile)
    shutil.move(srcfile, dstpath + fname)  # 移动文件
    print("move %s -> %s" % (srcfile, dstpath + fname))


src_dir = 'Z:/pingpangclips/xigua_video/video_person_tracking/000079/'  # 目标路径

dst_name = '000079_000028_FN000390_TID000065.avi'

# 有用素材
# dst_dir = 'Z:/pingpangclips/xigua_video/material_side侧面/'  # 目的路径
# # dst_dir = 'Z:/pingpangclips/xigua_video/material_front正面/'  # 目的路径
# # dst_dir = 'Z:/pingpangclips/xigua_video/material_slow慢动作/'  # 目的路径
# # dst_dir = 'Z:/pingpangclips/xigua_video/no_serve负样本/'  # 目的路径
# src_file_list = glob(src_dir + dst_name)  # glob获得路径下文件

# 无用素材
dst_dir = 'Z:/pingpangclips/xigua_video/no_action无用素材/'  # 全部移动
src_file_list = glob(src_dir + '*')  # glob获得路径下全部文件

if not src_file_list:
    print("%s not exist!" % dst_name)

for srcfile in src_file_list:
    mymovefile(srcfile, dst_dir)
