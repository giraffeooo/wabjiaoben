import glob
import re

import os.path as osp

def _process_dir(dir_path, relabel=False):
    img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
    pattern = re.compile(r'([-\d]+)_d(\d+)_v(\d)')

    pid_container = set()
    for img_path in sorted(img_paths):
        pid, display, view = map(int, pattern.search(img_path).groups())
        if pid == -1: continue  # junk images are just ignored
        pid_container.add(pid)
    pid2label = {pid: label for label, pid in enumerate(pid_container)}
    dataset = []
    for img_path in sorted(img_paths):
        pid, d, v = map(int, pattern.search(img_path).groups())
        if pid == -1: continue  # junk images are just ignored
        assert 0 <= display <= 1
        assert 0 <= view <= 3
        if relabel: pid = pid2label[pid]

        dataset.append((img_path, d, v))
    return dataset


if __name__=="__main__":
    dir_path='D:\AI\output\gallery'
    dataset = _process_dir(dir_path, relabel=False)
    print('1')