import glob
import shutil
import os
import pandas as pd
import logging
df = pd.read_excel('only_1000_images.xlsx', skiprows = 1)
empiar_ids = df['EMPIAR_ID']
gain_extensions = df['Gain Ext']

SOURCE_ADDRESS = '/gpfs/alpine/bif135/scratch/ashwind/CryoEM/data_downloads_dump_has_more_than1000/444_gainref_data/'
DESTINATION_ADDRESS = '/gpfs/alpine/bif135/scratch/ashwind/CryoEM/data_downloads/'

logging.basicConfig(filename='gainfiles_copy.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger2 = logging.getLogger()
logger2.setLevel(logging.DEBUG)

for i in range(len(empiar_ids)):
    destination_dir =  DESTINATION_ADDRESS + str(empiar_ids[i]) + '/gain/'
    gain = gain_extensions[i]
    if str(gain) == "nan":
        message = "No Gain or Motion Correction Files for " + str(empiar_ids[i])
        logger2.error(message)
    else:
        if len(gain_extensions[i]) == 2:
            micrographs_files = glob.glob(SOURCE_ADDRESS + str(empiar_ids[i]) + '/' + gain_extensions[i][0])
            micrographs_files.extend(glob.glob(SOURCE_ADDRESS + str(empiar_ids[i]) + '/' + gain_extensions[i][1]))
        else:
            micrographs_files = glob.glob(SOURCE_ADDRESS + str(empiar_ids[i]) + '/' + gain_extensions[i][0])
        try:
            c = 0
            for file in micrographs_files:
                f = file.split("/")[-1]

                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                shutil.copy2(file, destination_dir + f)
                c += 1
                if c >= 5:
                    break
            message = str(c) + " number of micrographs copied to " + str(destination_dir) + ' with extensions: ' + str(gain_extensions[i][0])
            logger2.info(message)
        except:
            message = "Micrographs failed to be copied to " + str(destination_dir) + ' with extensions: ' + str(gain_extensions[i][0])
            logger2.error(message)
