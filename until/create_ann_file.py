import os
from mmcv import load, dump
def traintest(dirpath, pklname, newpklname):
    os.chdir(dirpath)
    train = load('/root/pyskl/until/train.json') 
    test = load('/root/pyskl/until/test.json')
    annotations = load(pklname)
    split = dict()
    split['xsub_train'] = [x['vid_name'] for x in train] #指定训练集里样本名字
    split['xsub_val'] = [x['vid_name'] for x in test] #指定测试集里样本名字
    dump(dict(split=split, annotations=annotations), newpklname)  #最后用于训练的pkl文件名
 
    
if __name__ == '__main__':
 
    dirpath = '/root/pyskl/tools/data/Weizmann'
    pklname = '/root/pyskl/until/train.pkl'
    newpklname = '/root/pyskl/until/Weizmann_xsub_litehrnet.pkl'
    traintest(dirpath, pklname, newpklname)