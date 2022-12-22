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
print("Root Path: ",root_path)

xmlfilepath = dataset_save_path + '/Annotations/'
if not os.path.exists(xmlfilepath):
    os.mkdir(xmlfilepath)
imagefilepath = dataset_save_path + '/JPEGImages/'
if not os.path.exists(imagefilepath):
    os.mkdir(imagefilepath)

xml_files = []
# Move annotations to annotations folder
for filename in os.listdir(root_path):
    if filename.endswith('.xml'):
        xml_files.append(filename)
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
# total_xml = os.listdir(xmlfilepath)
num = len(xml_files)
list = range(num)
print("Total Number: ",num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)

# print("train and val size:", tv)
# print("train size:", tr)

ftrainval = open(txtsavepath + '/trainval.txt', 'a')
if dataset_type.strip() == 'train':
  datafile = open(txtsavepath + '/train.txt', 'w')
elif dataset_type.strip() == 'val':
  datafile = open(txtsavepath + '/val.txt', 'w')
elif dataset_type.strip() == 'test':
  datafile = open(txtsavepath + '/test.txt', 'w')

for i in list:
    name = xml_files[i][:-4] + '\n'
    if dataset_type.strip() == 'train' or dataset_type.strip() == 'val':
        ftrainval.write(name)
        if dataset_type.strip() == 'train':
            datafile.write(name)
        elif dataset_type.strip() == 'val':
            datafile.write(name)
    elif dataset_type.strip() == 'test':
        datafile.write(name)

datafile.close()
ftrainval.close()
