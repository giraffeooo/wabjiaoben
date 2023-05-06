'''提取video_frame的anchor,输出到train/test文件夹
    命名格式为instanceID_d(1/0)_v(1/2/3/4)_n，instanceID=0代表没有此商品，类比market1501查无此人
    d:(1纯商品/0模特上身)
    v(1正/2背/3左/4右)
    n是该商品的第n个anchor，避免命名重复'''
import glob
from PIL import Image
import os
import os.path
import json
annotation = r'D:\AI\demo_dataset\video_annotation'
video_frame = r'D:\AI\demo_dataset\video_frame'
an_dir = os.listdir(annotation)
img_dir = os.listdir(video_frame)
video_frame_annotation = [3, 4, 5, 6, 7, 8, 9, 2]   # 分别对应提取每一帧的annotation
# 一张图片的第一个anchor
for filename in img_dir:
    path = os.path.join(video_frame,filename)
    anno_dir = os.path.join(annotation, filename+'.json')
    with open(anno_dir, 'r', encoding='utf-8') as f:
        imgcrop = json.load(f)
        imgcrop = imgcrop['frames']
        img_list = os.listdir(path)
        img_list = sorted(img_list)
    for id, img in enumerate(img_list):
        img_path = os.path.join(path,img)
        img_open = Image.open(img_path)
        num = video_frame_annotation[id]
        imgcrop_frame = imgcrop[num]
        cf = 0 # 避免重复把之前的anchor覆盖了，图就变少了
        for n in imgcrop_frame['annotations']:
            xmin,ymin,xmax,ymax = n['box']
            instanID = n['instance_id']
            if instanID==0:
                instanID=-1
            display = n['display']
            viewpoint = n['viewpoint']
            box = img_open.crop((xmin,ymin,xmax,ymax))
            img_split = img.split('_')[-1].split('.')[0]
            anchor_filename = r'D:\AI\output\test'+'\\' + str(instanID) + '_d'+ str(display) + '_v'+ str(viewpoint) + '_'+img_split+ '_' +str(cf) +'.jpg'   # 表示这张图片第1个anchor
            box.save(anchor_filename)
            cf += 1


        # xmin,ymin,xmax,ymax = n['box']
        # instanID = n['instance_id']
        # if instanID==0:
        #     instanID=-1
        # display = n['display']
        # viewpoint = n['viewpoint']
        # box = img_open.crop((xmin,ymin,xmax,ymax))
        # img_split = img.split('_')[-1].split('.')[0]
        # anchor_filename = 'D:\AI\output\gallery'+'\\' + str(instanID) + '_d'+ str(display) + '_v'+ str(viewpoint) + '_'+img_split+'.jpg'   # 表示这张图片第1个anchor
        # box.save(anchor_filename)