import os
import pandas as pd
import numpy as np
from PIL import Image

im_path = '/home/math13/JR/kaggle/train'
csv_train = '/home/math13/JR/kaggle/train_ship_segmentations_v2.csv'

if __name__ == '__main__':
    
    df = pd.read_csv(csv_train)
    print(df.shape[0])

    
    num_of_ships = df.shape[0]
    print(num_of_ships)

    images = set()
    for line in range(num_of_ships):
        if df.iloc[line,0] not in images:
            images.add(df.iloc[line,0])
    print(len(images))
    count = 0
    ims = os.listdir(im_path)
    for im in ims:
        if im not in images:
            os.remove(os.path.join(im_path, im))
            count += 1
    print('%d images is deleted.'%(count))