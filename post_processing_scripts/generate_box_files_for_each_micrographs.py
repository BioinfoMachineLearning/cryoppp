#!/usr/bin/env python
# coding: utf-8

# # Generating box files for each micrographs


import glob
import os
import pandas as pd
import numpy as np

#Change this according to your structure of your CryoSPARC project

project_dir = '/home/*/*/CryoEMData/'

empiar_ids = ['10081','10289','11057'] #Example EMPIAR IDs
#Put corresponding particle diameter of each empiar id in pixel
#Divide Diameter in Angstron by Pixel Spacing
particle_diameters = [154,162,186]   #Example diameters of EMPIAR IDs


for j in range(len(empiar_ids)):
    filename = glob.glob(project_dir + empiar_ids[j] + '/metadata/*_particles_selected.csv')[0]
    print(filename)
    directory = filename.replace(filename.split('/')[-1], '')
    try:
        os.mkdir(directory + "coordinates", mode = 0o777)
    except:
        pass
    df = pd.read_csv(filename)
    df['Diameter'] = np.array([particle_diameters[j] for k in range(len(df['X-Coordinate']))])
    files = df['Micrographs Filename'].unique()
    for f in files:
        f_name = f.split('.')[0]
        df_box = df[df['Micrographs Filename'] == f]
        df_coord = df_box.loc[:, ['X-Coordinate', 'Y-Coordinate', 'Diameter']]
        df_coord.to_csv(directory + "coordinates/" + f_name + '.csv', index=False)






