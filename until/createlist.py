import os

from pyskl.smp import mwlines


def writeList(dirpath, name):
    path_train = os.path.join(dirpath, 'train')
    path_test = os.path.join(dirpath, 'test')
    trainfile_list = os.listdir(path_train)
    testfile_list = os.listdir(path_test)

    train = []
    for train_name in trainfile_list:
        traindit = {}
        sp = train_name.split('_')

        traindit['vid_name'] = train_name
        traindit['label'] = sp[1].replace('.avi', '')
        train.append(traindit)
    test = []
    for test_name in testfile_list:
        testdit = {}
        sp = test_name.split('_')
        testdit['vid_name'] = test_name
        testdit['label'] = sp[1].replace('.avi', '')
        test.append(testdit)

    tmpl1 = os.path.join(path_train, '{}')
    lines1 = [(tmpl1 + ' {}').format(x['vid_name'], x['label']) for x in train]

    tmpl2 = os.path.join(path_test, '{}')
    lines2 = [(tmpl2 + ' {}').format(x['vid_name'], x['label']) for x in test]
    lines = lines1 + lines2
    print(name) # 这个是文件名 name是Weizmann.list 
    mwlines(lines, name) #这样就是在createlist的同级目录了


writeList(r'/root/pyskl/tools/data/Weizmann', '/root/pyskl/until/Weizmann.list') 

print("OK")
