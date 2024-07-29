import os
import decord
import json
def writeJson(path_train, jsonpath):
    outpot_list = []
    trainfile_list = os.listdir(path_train)
    for train_name in trainfile_list:
        traindit = {}
        sp = train_name.split('_')
        traindit['vid_name'] = train_name.replace('.avi', '')
        traindit['label'] = int(sp[1].replace('.avi', ''))
        traindit['start_frame'] = 0

        video_path = os.path.join(path_train, train_name)
        vid = decord.VideoReader(video_path)
        traindit['end_frame'] = len(vid)
        outpot_list.append(traindit.copy())
        # print(outpot_list)
    with open(rf'{jsonpath}', 'w',encoding='utf-8') as outfile:
        json.dump(outpot_list, outfile)
writeJson(r'/root/pyskl/tools/data/Weizmann/train', '/root/pyskl/until/train.json')
writeJson(r'/root/pyskl/tools/data/Weizmann/test', '/root/pyskl/until/test.json')
