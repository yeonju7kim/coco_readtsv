# -*- encoding: utf-8 -*-
'''
@File    :   tsv_read.py   
@Contact :   emac.li@cloudminds.com
@License :   (C)Copyright 2018-2021
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022-11-09 오후 8:57   Emac.li      1.0         None
'''
import pandas as pd
from PIL import Image
import io, base64

from tqdm import tqdm

tsvfile = 'D:\\data\\image_captioning\\caption_data\\caption_test.tsv'
# tsvfile = 'D:\\data\\image_captioning\\caption_data\\caption_val.tsv'
# tsvfile = 'D:\\data\\image_captioning\\caption_data\\caption_stage1_train.tsv'
# tsvfile = 'D:\\data\\image_captioning\\caption_data\\caption_stage2_train.tsv'
dstpath = 'D:\\data\\image_captioning\\caption_data\\all'
def main():
    read_coco_tsv(tsvfile, dstpath)

def read_coco_tsv(filename, dst_path):
    df = pd.read_csv(filename, sep = '\t')
    test_list = [a for a in df.iterrows()]
    for data in tqdm(test_list):
        caption_num = data[1][0]
        image_num = data[1][1]
        caption = data[1][2]
        tag = data[1][3]
        img = data[1][4]
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(img, "utf-8"))))
        img.save(dst_path + f'\\{str(image_num).zfill(6)}.jpg')

if __name__ == "__main__":
    main()