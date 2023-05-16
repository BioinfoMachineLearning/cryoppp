def download_micrographs(empiar_id, data_download_location, data_link):
    # For Downloading Data Files

    data_download_path = os.path.join(data_download_location, str(empiar_id), 'micrographs')
    if not os.path.exists(data_download_path):
        os.makedirs(data_download_path) 
        
    df = pd.read_excel('micrographs_download_catalogue.xlsx', sheet_name=str(empiar_id))
    micrographs_names = df['Micrographs'].dropna()
    start_time = time.time()
    for j in range(len(micrographs_names)):
        try:
            download_url = os.path.join('https://ftp.ebi.ac.uk/empiar/world_availability/', data_link, micrographs_names[j])
            print(f"Downloading {j+1} out of {len(micrographs_names)}")
            print(download_url)
            wget.download(download_url, out = data_download_path)
        except:
            print(f"Error downloading micrographs of {str(empiar_id)}")
    print("--- %s seconds ---" % (time.time() - start_time))    





def download_gain_files(empiar_id, gain_download_location, gain_link):
    # For Downloading Data Files

    try:    
        df = pd.read_excel('micrographs_download_catalogue.xlsx', sheet_name=str(empiar_id))
        gain_file_names = df['Gain'].dropna()
        start_time = time.time()
        gain_download_path = os.path.join(gain_download_location, str(empiar_id), 'gain')
        if not os.path.exists(gain_download_path):
            os.makedirs(gain_download_path) 
        for k in range(len(gain_file_names)):
            try:
                download_url = os.path.join('https://ftp.ebi.ac.uk/empiar/world_availability/', gain_link, gain_file_names[k])
                print(f"Downloading {k+1} out of {len(gain_file_names)}")
                print(download_url)
                wget.download(download_url, out = gain_download_path)
            except:
                print(f"Error downloading gain file of {str(empiar_id)}")
        print("--- %s seconds ---" % (time.time() - start_time))
    except:
        print(f"No associated gain files for EMPIAR ID : {empiar_id}")

def main():
    print("*********** Welcome to Data Downloader **********************")
    print("\nDownloading all the data may require a significant amount of time !")
    print("It depends upon the speed of internet and you could parallelize download for each EMPIAR ID !\n")
    print("\n")
    download_location = input("Please, provide the download path for files: (Example: /home/user/Downloads)")
    approach = input("Do you want to download all EMPIAR IDs ? \n\nPress Y if yes else type a particular EMPIAR ID (Eg: 10005) ")

    df = pd.read_excel('micrographs_download_catalogue.xlsx', sheet_name='EMPIAR-IDs')
    empiar_ids = df['EMPIAR_ID']
    data_links = df['Data_Link']
    gain_links = df['Gain_Link']

    try:

        if approach == "Y" or approach == 'y' :
            for i in range(len(empiar_ids)):
                #running for individual 
                try:
                    empiar_id = empiar_ids[i]
                    data_link = data_links[i]
                    gain_link = gain_links[i]
                    print(f"********************** EMPIAR ID : {empiar_id} **********************")

                    # For Downloading Data Files
                    try:
                        download_micrographs(empiar_id, download_location, data_link)
                    except:
                        print("Error downloading images files")

                    # For Downloading Gain Files
                    try:
                        download_gain_files(empiar_id, download_location, gain_link)
                    except:
                        print("Error downloading gain files")
                except:
                    print("Error downloading data")
        else:
            empiar_id = int(approach)
            df1 = df.loc[df['EMPIAR_ID'] == empiar_id]        
            data_link = list(df1['Data_Link'])[0]
            gain_link = list(df1['Gain_Link'])[0]
            print(f"********************** EMPIAR ID : {empiar_id} **********************")

            #For Downloading Data Files
            try:
                download_micrographs(empiar_id, download_location, data_link)
            except:
                print("Error downloading images files")

            #For Downloading Gain Files
            try:
                download_gain_files(empiar_id, download_location, gain_link)
            except:
                print("Error downloading gain files")

    except:
        print("Please try again with appropriate input")
        
try:
    import numpy as np
    import pandas as pd
    import requests
    from ftplib import *
    import ftplib
    import wget
    import os
    import time
    import glob
    main()
except:
    print("Please install following libraries by applying the following command!")
    print("\npip install numpy pandas requests wget openpyxl\n")

