
import os
# synthtiger_root_folder='synthtiger_12M'
# trdg_labels_file='trdg_12M_images_trdg_labels.txt'

synthtiger_root_folder='/home/gaurav/scratch/trdg/trdg/output/gujarati/train/synthtiger'
trdg_labels_file='/home/gaurav/scratch/trdg/trdg/output/gujarati/train/trdg_trdg_labels.txt'

with open(os.path.join(synthtiger_root_folder,'synthtiger_gt.txt'),'r') as f, open(trdg_labels_file,'r') as f2, open('final_labels.txt','w') as f3:
    lines1=f.readlines()
    lines2=f2.readlines()
    for line in lines1:
        f3.write("{}/{}".format(synthtiger_root_folder, line))
    for line in lines2:
        f3.write(line)
f.close()
f2.close()
f3.close()