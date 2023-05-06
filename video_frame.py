'''             提取视频标注帧的脚本            '''

import os
import cv2
import argparse
import json
import shutil
import math
'''                         修改参数区                       '''
videos_src_path = r'D:\AI\demo_dataset\video'
#videos_src_path = args.path
print('now processing videos from {}'.format(videos_src_path))
videos_save_path = r'D:\AI\demo_dataset\video_frame'
video_annotation_path = r'D:\AI\demo_dataset\video_annotation'

if not os.path.exists(videos_save_path):
    os.makedirs(videos_save_path)
file_count = 0
videos = os.listdir(videos_src_path)
for each_video in videos:

    file_count += 1
    each_video_name = each_video.split('.')[0]  # video的名字，也就是instance ID
    each_video_full_path = os.path.join(videos_src_path, each_video)    # video path
    each_videoannotation_full_path = os.path.join(video_annotation_path, each_video_name+'.json')
    img_path = os.path.join(videos_save_path, each_video_name)
    if os.path.exists(img_path):
        shutil.rmtree(img_path) # 如果存在就删除
    os.mkdir(img_path)
    cap = cv2.VideoCapture(each_video_full_path)
    frames_num = cap.get(7) # 视频总帧数
    rate = cap.get(5)
    duration = round(frames_num / rate)
    print("video {} is setting\ntime length:{}s".format(each_video_name, duration))
    print(file_count)
    c = 0
    key_frame=[80, 120, 160, 200, 240, 280, 320, 360]
    ret = True
    # with open(each_videoannotation_full_path, 'r') as f:
    #     video_annotation = json.load(f)
    #     for frame_index in enumerate(video_annotation['frames']):
    #         key_frame.append(frame_index[1]['frame_index'])

    while ret:
        ret, frame = cap.read()

        if frame is None:
            continue
        if (c in key_frame) & (c >= 80):
            cv2.imencode('.jpg', frame)[1].tofile(img_path + '/' + '{}.jpg'.format(c))
        c += 1
print('\nvideo numbers:', str(file_count), '\nAll is done ,thanks')
