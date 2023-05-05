'''修改img和json的名字'''
import os

root_path = 'D:\AI\demo_dataset\image_annotation'  # 要修改的图像所在的文件夹路径

filelist = os.listdir(root_path)  # 遍历文件夹       filelist=[a,b]

for item in filelist:
    path = os.path.join(root_path,item)
    for img in os.listdir(path):
        if img.endswith('.jpg'):    # 修改图片名
            src = os.path.join(os.path.abspath(path), img)  # 原本的名称
            up_name = os.path.basename(path)
            dst = os.path.join(os.path.abspath(path),
                               os.path.basename(path) + '_' + img)  # 这里我把格式统一改成了 .jpg
        elif img.endswith('.json'):    # 修改图片名
            src = os.path.join(os.path.abspath(path), img)  # 原本的名称
            up_name = os.path.basename(path)
            dst = os.path.join(os.path.abspath(path),
                               os.path.basename(path) + '_' + img)  # 这里我把格式统一改成了 .jpg
        try:
            os.rename(src, dst)  # 意思是将 src 替换为 dst

            print('rename from %s to %s' % (src, dst))
        except:
            continue
print('ending...')