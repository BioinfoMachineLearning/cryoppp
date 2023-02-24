import glob
import shutil
import os
import pandas as pd
import logging
df = pd.read_excel('only_1000_images.xlsx', skiprows = 1)
empiar_ids = df['EMPIAR_ID']
micrographs_extensions = df['Image Ext']

SOURCE_ADDRESS = '/gpfs/alpine/bif135/scratch/ashwind/CryoEM/data_downloads_dump_has_more_than1000/444_micrographs_data/'
DESTINATION_ADDRESS = '/gpfs/alpine/bif135/scratch/ashwind/CryoEM/data_downloads/'

logging.basicConfig(filename='micrographs.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

for i in range(len(empiar_ids)):
    micrographs_files = glob.glob(SOURCE_ADDRESS + str(empiar_ids[i]) + '/' + micrographs_extensions[i])
    destination_dir =  DESTINATION_ADDRESS + str(empiar_ids[i]) + '/micrograph_images/'
    try:
        c = 0
        for file in micrographs_files:
            f = file.split("/")[-1]
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            shutil.copy2(file, destination_dir + f)
            c += 1
            if c >= 1000:
                break
        message = str(c) + " number of micrographs copied to " + str(destination_dir) + ' with extensions: ' + str(micrographs_extensions[i])
        logger.info(message)
    except:
        message = "Micrographs failed to be copied for " + str(destination_dir) + ' with extensions: ' + str(micrographs_extensions[i])
        logger.error(message)
