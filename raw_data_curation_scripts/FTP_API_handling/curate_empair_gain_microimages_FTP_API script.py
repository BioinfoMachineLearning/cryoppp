import numpy as np
import pandas as pd
import requests
from ftplib import *
import ftplib
import wget
import os
import time
import glob

df = pd.read_excel('Download_List.xlsx')
empiar_ids = df['EMPIAR_ID']
data_link = df['Data_Link']
gain_link = df['Gain_Link']


for i in range(len(empiar_ids)):
    #running for individual 
    try:
        empiar_id = empiar_ids[i]
        print(empiar_id)


        # For Downloading Data Files
        try:
            data_download_path = f'/home/ad256/Ashwin/Projects/cryoEM/repo/data_downloads/444_data/{empiar_id}/data'
            if not os.path.exists(data_download_path):
                os.makedirs(data_download_path)   

            ftp = FTP("ftp.ebi.ac.uk", timeout=None)
            ftp.login()    
            data_path = data_link[i][22:]
            print(data_path)
            start_time = time.time()

            ftp.cwd(data_path)
            image_list = ftp.nlst()
            print("--- %s seconds ---" % (time.time() - start_time))        

            for image in (image_list):
                tiff_extension = image[-4:]
                tif_extension = image[-3:]
                mrc_extension = image[-3:]
                if (tiff_extension == 'tiff' or mrc_extension == 'mrc' or tif_extension == 'tif'):
                    download_url  = data_link[i] + '/' + image
                    print(download_url)
                    wget.download(download_url, out = data_download_path)
            print("--- %s seconds ---" % (time.time() - start_time))
        except:
            print("Error downloading images files")
        
        # For Downloading Gain Files
        try:
            gain_download_path = f'/home/ad256/Ashwin/Projects/cryoEM/repo/data_downloads/444_data/{empiar_id}/gain'
            if not os.path.exists(gain_download_path):
                os.makedirs(gain_download_path)   

            ftp = FTP("ftp.ebi.ac.uk", timeout=None)
            ftp.login()    
            gain_path = gain_link[i][22:]
            print(gain_path)
            start_time = time.time()

            ftp.cwd(data_path)
            gain_list = ftp.nlst()
            print("--- %s seconds ---" % (time.time() - start_time))        

            for gain in (gain_list):
                tiff_extension = gain[-4:]
                tif_extension = gain[-3:]
                mrc_extension = gain[-3:]
                if (tiff_extension == 'tiff' or mrc_extension == 'mrc' or tif_extension == 'tif'):
                    download_url  = gain_link[i] + '/' + gain
                    print(download_url)
                    wget.download(download_url, out = gain_download_path)

            print("--- %s seconds ---" % (time.time() - start_time))
        except:
            print("Error downloading gain files")
    except:
        print("Error downloading data")
        
