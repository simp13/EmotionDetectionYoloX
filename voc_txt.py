import os
import random
import sys
import shutil
from pathlib import Path

if len(sys.argv) < 3:
    print("no directory specified, please input target directory")
    exit()

root_path = sys.argv[1]
dataset_type = sys.argv[2]
dataset_save_path = sys.argv[3]

xmlfilepath = dataset_save_path + '/Annotations/'
if not os.path.exists(xmlfilepath):
    os.mkdir(xmlfilepath)
imagefilepath = dataset_save_path + '/JPEGImages/'
if not os.path.exists(imagefilepath):
    os.mkdir(imagefilepath)

# Move annotations to annotations folder
for filename in os.listdir(root_path):
    if filename.endswith('.xml'):
        with open(os.path.join(root_path, filename)) as f:
            Path(root_path + filename).rename(xmlfilepath + filename)

    if filename.endswith('.jpg'):
        with open(os.path.join(root_path, filename)) as f:
            Path(root_path + filename).rename(imagefilepath + filename)


txtsavepath = dataset_save_path + '/ImageSets/Main'

if not os.path.exists(root_path):
    print("cannot find such directory: " + root_path)
    exit()

if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

# trainval_percent = 0.9
# train_percent = 0.8
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
print("Total Number: ",num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)

# print("train and val size:", tv)
# print("train size:", tr)
ftrainval = open(txtsavepath + '/trainval.txt', 'a')
ftest = open(txtsavepath + '/test.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if dataset_type.strip() == 'train' or dataset_type.strip() == 'val':
        ftrainval.write(name)
        if dataset_type.strip() == 'train':
            ftrain.write(name)
        elif dataset_type.strip() == 'val':
            fval.write(name)
    elif dataset_type.strip() == 'test':
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
