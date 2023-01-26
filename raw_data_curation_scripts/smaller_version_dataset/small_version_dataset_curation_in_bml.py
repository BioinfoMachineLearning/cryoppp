import glob
import shutil
import os
import pandas as pd
import logging
import paramiko

df = pd.read_excel('2_list.xlsx', skiprows = 1)
empiar_ids = df['EMPIAR_ID']
# empiar_ids = ['10467', '10495', '10682']

SOURCE_ADDRESS = '/gpfs/alpine/bif135/scratch/ashwind/CryoEM/data_curation/'
DESTINATION_ADDRESS = '/bml/CryoEM/particle_picking/small_version_particle_picking_dataset/'

#Initializing SSH Client
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('multicom.eecs.missouri.edu', username='username', password='password', port=22)
sftp_client = ssh.open_sftp()


logging.basicConfig(filename='smaller_version_micrographs.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

for i in range(len(empiar_ids)):
    micrographs_files = glob.glob(SOURCE_ADDRESS + str(empiar_ids[i]) + '/micrograph_images/*')
    destination_dir =  DESTINATION_ADDRESS + str(empiar_ids[i]) + '/micrograph_images/'
    try:
        c = 0
        for file in micrographs_files:
            f = file.split("/")[-1]
            print(f)
#             if not os.path.exists(destination_dir):
#                 os.makedirs(destination_dir, 0o777)
#             shutil.copy2(file, destination_dir + f)
            sftp_client.put(file, destination_dir + f)
            c += 1
            if c >= 20:
                break
        message = str(c) + " number of micrographs copied to " + str(destination_dir)
        logger.info(message)
    except:
        message = "Micrographs failed to be copied for " + str(destination_dir)
        logger.error(message)
sftp_client.close()
ssh.close()



df = pd.read_excel('EMPAIR_database_protein_download_catalog_v0.1.xlsx', skiprows = 1)
# empiar_ids = ['10467', '10495', '10682']

SOURCE_ADDRESS = '/gpfs/alpine/bif135/scratch/ashwind/CryoEM/data_curation/'
DESTINATION_ADDRESS = '/bml/CryoEM/particle_picking/small_version_particle_picking_dataset/'

#Initializing SSH Client
ssh = paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('lily.engineering.missouri.edu', username='username', password='password', port=22)
sftp_client = ssh.open_sftp()


logging.basicConfig(filename='gainfiles_copy.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger2 = logging.getLogger()
logger2.setLevel(logging.DEBUG)

for i in range(len(empiar_ids)):
    gain_files = glob.glob(SOURCE_ADDRESS + str(empiar_ids[i]) + '/gain/*')
    destination_dir =  DESTINATION_ADDRESS + str(empiar_ids[i]) + '/gain/'
    try:
        c = 0
        for file in gain_files:
            f = file.split("/")[-1]
            print(f)

#             if not os.path.exists(destination_dir):
#                 os.makedirs(destination_dir)
#             shutil.copy2(file, destination_dir + f)
            sftp_client.put(file, destination_dir + f)
            c += 1
            if c >= 5:
                break
        message = str(c) + " number of gainfiles copied to " + str(destination_dir)
        logger2.info(message)
    except:
        message = "Gainfiles failed to be copied to " + str(destination_dir)
        logger2.error(message)
        
sftp_client.close()
ssh.close()
