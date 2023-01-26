import glob
import os
import pandas as pd
import numpy as np

#Change this according to your structure of CryoEM_Final_Dataset directoryor 
#comment this line if project dir has not changed
project_dir = '/bml/CryoEM/CryoEM_Final_Dataset/'


empiar_ids = ['10737', '10387', '10532', '10240', '10005', '10017', '10075', '10184', '10059', '10406', '10590', '10093']
#Put corresponding particle diameter of each empiar id in pixel
# Divide Diameter in Angstron by Pixel Spacing
# particle_diameters = [186, 265]   

for j in range(len(empiar_ids)):
    filename = glob.glob(project_dir + empiar_ids[j] + '/ground_truth/*_particles_selected.csv')[0]
    # print(filename)
    # print(empiar_ids[j])
    # print(particle_diameters[j])
    directory = filename.replace(filename.split('/')[-1], '')
    df = pd.read_csv(filename)
    # df['Diameter'] = np.array([particle_diameters[j] for k in range(len(df['X-Coordinate']))])
    files = df['Micrographs Filename'].unique()
    print("Number of Micrographs for "+ empiar_ids[j] , len(files))
    # for f in files:
    #     f_name = f[:-4]
    #     df_coord = df[df['Micrographs Filename'] == f]
    #     df_box = df_coord.loc[:, ['X-Coordinate', 'Y-Coordinate', 'Diameter', 'Angle-Psi', 'Origin X (Ang)', 'Origin Y (Ang)', 'Defocus U', 'Defocus V', 'Defocus Angle', 'Phase Shift', 'CTF B Factor']]
    #     df_box.to_csv(directory + "particle_coordinates/" + f_name + '.csv', index=False)
    # print("Completed for "+ empiar_ids[j])