import numpy as np
import pandas as pd
import requests
from ftplib import *
import ftplib
import wget
import os
import time


#running for individual 
empiar_id = '10970'
print(empiar_id)

data_download_path = f'/home/ad256/Ashwin/Projects/cryoEM/repo/data_downloads/444_data/{empiar_id}'
if not os.path.exists(data_download_path):
    os.makedirs(data_download_path)   
    
start_time = time.time()

ftp = FTP("ftp.ebi.ac.uk", timeout=None)
ftp.login()    
data_path = f'/empiar/world_availability/{empiar_id}/data/VcINDY-choline_empiar/class_2'
ftp.cwd(data_path)
image_list = ftp.nlst()
cap = 0
for image in (image_list):
    tiff_extension = image[-4:]
    mrc_extension = image[-3:]
    if (tiff_extension == 'tiff' or mrc_extension == 'mrc') and (cap <10):
        print("\n This is the ", cap ,"th file")
        download_url  = f'https://ftp.ebi.ac.uk/empiar/world_availability/{empiar_id}/data/VcINDY-choline_empiar/class_2/{image}'
        print(download_url)
        wget.download(download_url, out = data_download_path)
        cap= cap+1

print("--- %s seconds ---" % (time.time() - start_time))        
        
        