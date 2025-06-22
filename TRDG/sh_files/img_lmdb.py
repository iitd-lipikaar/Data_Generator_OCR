import os
import lmdb
import cv2
import numpy as np


from multiprocessing import Pool
from tqdm import tqdm
import fire

def checkImageIsValid(imageBin):
    """Check if image is valid"""
    if imageBin is None:
        return False
    imageBuf = np.frombuffer(imageBin, dtype=np.uint8)
    img = cv2.imdecode(imageBuf, cv2.IMREAD_COLOR)
    imgH, imgW = img.shape[0], img.shape[1]
    if imgH * imgW == 0:
        return False
    return True
    
def writeCache(env, cache):
    """Write cache to LMDB"""
    with env.begin(write=True) as txn:
        for k, v in cache.items():
            txn.put(k, v)

def img_worker(args):
    Input_ImageFolder, outputPath, imagePath, label, idx = args
    
    imagePath = os.path.join(Input_ImageFolder, imagePath)
    
    if not os.path.exists(imagePath):
        # print('%s Image does not exist' % imagePath)
        with open(outputPath + '/error_image_log.txt', 'a') as log:
            log.write('%s Image Does Not Exist\n' % str(imagePath))
        return None
    
    with open(imagePath, 'rb') as f:
        imageBin = f.read()

    try:
        if not checkImageIsValid(imageBin):
            print('%s is not a valid image' % imagePath)
            with open(outputPath + '/error_image_log.txt', 'a') as log:
                log.write('%s Image is not a Valid Image\n' % str(imagePath))
            return None
    except:
        print('Image Data Error occurred', imagePath)
        with open(outputPath + '/error_image_log.txt', 'a') as log:
            log.write('%s Image Data Error Occurred\n' % str(imagePath))
        return None

    imageBuf = np.frombuffer(imageBin, dtype=np.uint8)
    img = cv2.imdecode(imageBuf, cv2.IMREAD_COLOR)
    imageBin = cv2.imencode('.jpg', img)[1].tobytes()
        
    return (imageBin, label)
        


def createDataset(Input_ImageFolder, Input_gtFile, outputPath, num_processes=40):
    
    os.makedirs(outputPath, exist_ok=True)
    env = lmdb.open(outputPath, map_size=1099511627776)
    cache = {}


    with open(Input_gtFile, 'r') as f:
        lines = f.readlines()
    
    total_images = len(lines)
    print("Total No of Lines in GT File (not Total Images) =", total_images)

    final_img_count=0
    args_list=[]
    for i in range(total_images):
        line = lines[i]
        line = line.strip()
        parts = line.split('\t', 1)
        if len(parts) == 1:
            parts = line.split(' ')
        if len(parts) == 1:
            print('Label is empty %s' % line)
            with open(outputPath + '/error_image_log.txt', 'a') as log:
                log.write('Label is empty %s\n' % line)
            continue
        final_img_count+=1
        imagePath, label = parts[0], parts[1]
        args_list.append((Input_ImageFolder, outputPath, imagePath, label, i+1)) #i+1 i.e. idx is not used in the img_worker function, by the way
    
    # print(args_list) #Only for Analysis Purpose. DoNot Uncomment
    print("No. Of Lines with non-empty Labels. There may be Images with missing path out of these too.", final_img_count)
        
    with Pool(num_processes) as p:    
        results = list(tqdm(p.imap(img_worker, args_list), total=final_img_count))

    count=1
    for r in results:
        if r is None:
            continue

        imageBin, label = r

        imageKey = 'image-%09d'.encode() % count
        labelKey = 'label-%09d'.encode() % count
        
        cache[imageKey] = imageBin
        cache[labelKey] = label.encode()

        if count % 1000 == 0:
            writeCache(env, cache)                 
            cache = {}
            print('Processed %d / %d images' % (count, final_img_count))
        
        count += 1


    count-=1
    cache['num-samples'.encode()] = str(count).encode()
    writeCache(env, cache)
    
    env.close()
    print('Created dataset with %d samples' % count)


if __name__ == '__main__':
    fire.Fire(createDataset)

# # Define your Input_ImageFolder, Input_gtFile, and outputPath
# Input_ImageFolder = 'iiith_assamese_lmdb_reconstructed_1'
# Input_gtFile = 'iiith_assamese_lmdb_reconstructed_1/gt.txt'
# outputPath = 'lmdb_NEW_3'

# createDataset(Input_ImageFolder, Input_gtFile, outputPath, num_processes=5)  # Adjust num_processes as needed



# python create_lmdb_fire_pool.py --Input_ImageFolder "1M" --Input_gtFile "1M/gt.txt" --outputPath "1M_lmdb" --num_processes=55

# python create_lmdb_fire_pool.py --Input_ImageFolder "iiith_assamese_lmdb_reconstructed_1" --Input_gtFile "iiith_assamese_lmdb_reconstructed_1/gt.txt" --outputPath "lmdb_NEW_3" --num_processes=55

# python copy7.py --Input_ImageFolder "iiith_assamese_lmdb_reconstructed_1" --Input_gtFile "iiith_assamese_lmdb_reconstructed_1/gt.txt" --outputPath "lmdb_NEW_11" --num_processes=55

# python FINAL_CREATE_LMDB_POOL_FIRE_Nishit.py --Input_ImageFolder "validation_5M/" --Input_gtFile "validation_5M/final_labels.txt" --outputPath "validation_5M_lmdb" --num_processes=55

# python FINAL_CREATE_LMDB_POOL_FIRE_Nishit.py --Input_ImageFolder "output" --Input_gtFile "output/final_labels.txt" --outputPath "train_24M_lmdb" --num_processes=55

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg/trdg/output/hindi/train" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg/trdg/output/hindi/train/trdg_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_hindi/data/train/synth/trdg6" --num_processes=55