#!/usr/bin/env python
# coding: utf-8
# # Converting star files to csv

# # Converting particles_selected and particles_excluded star files to csv files in the original cs-empiar cryosparc directories


import pandas as pd
import glob

#Change this according to your structure of Cryo EM project directory or 
#comment this line if project dir has not changed
project_dir = '/home/*/*/CryoEMData/'

filenames = glob.glob(project_dir + '*/CS-empiar*/exports/groups/*/*particles*.star')  #Replace front * by empiar-id 
                                                            # directory(eg: 11111) if, you want to convert project by project


for filename in filenames:
    file = filename.split('/')[-1]
    directory = filename.replace(file, '')
    original_df = pd.read_csv(filename, skiprows = 30)
    records = original_df['_rlnClassNumber #14 ']

    columns_names = ['Particles Filename', 'Micrographs Filename', 'X-Coordinate', 'Y-Coordinate', 'Angle-Psi', 'Origin X (Ang)',
                    'Origin Y (Ang)', 'Defocus U', 'Defocus V', 'Defocus Angle', 'Phase Shift', 'CTF B Factor', 'Optics Group', 'Class Number']
    
    try:
        df = pd.DataFrame()
        particle_filename = []
        micrograph_filename = []
        x_coordinate = []
        y_coordinate = []
        angle_psi = []
        origin_x_angst = []
        origin_y_angst = []
        defocus_u = []
        defocus_v = []
        defocus_angle = []
        phase_shift = []
        ctf_b_factor = []
        optics_group = []
        class_number = []
        for i in range(len(records)):
            values = records[i].split(' ')
            pf = values[0].split('/')[2][22:]
            mf = values[1].split('/')[2][22:]
            try:
                pf = pf.replace('_patch_aligned_doseweighted','')
                mf = mf.replace('_patch_aligned_doseweighted','')
            except:
                pass
            particle_filename.append(pf)
            micrograph_filename.append(mf)
            x_coordinate.append(values[2])
            y_coordinate.append(values[3])
            angle_psi.append(values[4])
            origin_x_angst.append(values[5])
            origin_y_angst.append(values[6])
            defocus_u.append(values[7])
            defocus_v.append(values[8])
            defocus_angle.append(values[9])
            phase_shift.append(values[10])
            ctf_b_factor.append(values[11])
            optics_group.append(values[12])
            class_number.append(values[13])
        df.insert(0, columns_names[0], particle_filename)
        df.insert(1, columns_names[1], micrograph_filename)
        df.insert(2, columns_names[2], x_coordinate)
        df.insert(3, columns_names[3], y_coordinate)
        df.insert(4, columns_names[4], angle_psi)
        df.insert(5, columns_names[5], origin_x_angst)
        df.insert(6, columns_names[6], origin_y_angst)
        df.insert(7, columns_names[7], defocus_u)
        df.insert(8, columns_names[8], defocus_v)
        df.insert(9, columns_names[9], defocus_angle)
        df.insert(10, columns_names[10], phase_shift)
        df.insert(11, columns_names[11], ctf_b_factor)
        df.insert(12, columns_names[12], optics_group)
        df.insert(13, columns_names[13], class_number)

        df.to_csv(directory + file.split('.')[0] + '.csv', index = False)
        print("Conversion success for ", filename)
    except:
        try:
            df = pd.DataFrame()
            particle_filename = []
            micrograph_filename = []
            x_coordinate = []
            y_coordinate = []
            angle_psi = []
            origin_x_angst = []
            origin_y_angst = []
            defocus_u = []
            defocus_v = []
            defocus_angle = []
            phase_shift = []
            ctf_b_factor = []
            optics_group = []
            class_number = []
            for i in range(len(records)):
                values = records[i].split(' ')
                vals = records[i].split('/')
                pf = vals[2].split('"')[0][22:]
                mf = vals[4].split('"')[0][22:]
                try:
                    pf = pf.replace('_patch_aligned_doseweighted','')
                    mf = mf.replace('_patch_aligned_doseweighted','')
                except:
                    pass
                particle_filename.append(pf)
                micrograph_filename.append(mf)
                x_coordinate.append(values[-12])
                y_coordinate.append(values[-11])
                angle_psi.append(values[-10])
                origin_x_angst.append(values[-9])
                origin_y_angst.append(values[-8])
                defocus_u.append(values[-7])
                defocus_v.append(values[-6])
                defocus_angle.append(values[-5])
                phase_shift.append(values[-4])
                ctf_b_factor.append(values[-3])
                optics_group.append(values[-2])
                class_number.append(values[-1])
            df.insert(0, columns_names[0], particle_filename)
            df.insert(1, columns_names[1], micrograph_filename)
            df.insert(2, columns_names[2], x_coordinate)
            df.insert(3, columns_names[3], y_coordinate)
            df.insert(4, columns_names[4], angle_psi)
            df.insert(5, columns_names[5], origin_x_angst)
            df.insert(6, columns_names[6], origin_y_angst)
            df.insert(7, columns_names[7], defocus_u)
            df.insert(8, columns_names[8], defocus_v)
            df.insert(9, columns_names[9], defocus_angle)
            df.insert(10, columns_names[10], phase_shift)
            df.insert(11, columns_names[11], ctf_b_factor)
            df.insert(12, columns_names[12], optics_group)
            df.insert(13, columns_names[13], class_number)

            df.to_csv(directory + file.split('.')[0] + '.csv', index = False)
            print("Conversion success for ", filename)
        except:
            print("Conversion Failure due to inconsistency in micrographs filename for ", filename)


# #   Organizing Files
Create a CryoEM_Final_Dataset Directory
Then inside, create directory with empiar-id. For eg: 11111
    - Inside each empiar-id directory create:
        - a directory called "metadata" to store star files and csv files
        - a directory called "micrographs" to store original micrographs
        - a directory called "gain" to store gain correction files
        - a directory called "particles_stack" to store particles MRC files
# # Renaming file name of particles_stack directory according to .csv files



import glob
import os

#Change this according to your structure of CryoEM_Final_Dataset directory
project_dir = '/home/*/*/CryoEMData/'

filenames = glob.glob(project_dir + '*/particles_stack/*') #Replace front * by empiar-id directory(eg: 11111) if, 
                                                            # you want to convert project by project
print(filenames)

for filename in filenames:
    file_n = filename.split("/")[-1]
    dir = filename.replace(file_n, '')
    fn = file_n[22:]
    try:
        fn = fn.replace('_patch_aligned_doseweighted','')
    except:
        pass
    destination_filename = dir + '/' + fn
    os.rename(filename, destination_filename) #(source_filename, destination_filename)


# # Renaming file name of micrographs directory according to .csv files



import glob
import os

#Change this according to your structure of CryoEM_Final_Dataset directoryor 
#comment this line if project dir has not changed
project_dir = '/home/*/*/CryoEMData/'

filenames = glob.glob(project_dir + '*/micrographs/*')      #Replace front * by empiar-id directory(eg: 11111) if, 
                                                            # you want to convert project by project



for filename in filenames:
    file_n = filename.split("/")[-1]
    dir = filename.replace(file_n, '')
    try:
        fn = file_n.replace('_patch_aligned_doseweighted','')
    except:
        pass
    destination_filename = dir + '/' + fn
    os.rename(filename, destination_filename) #(source_filename, destination_filename)

