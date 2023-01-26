import glob
import os
import pandas as pd
import numpy as np

empiar_ids = ['11057', '10576']
# empiar_ids = ['10576']

for m in range(len(empiar_ids)):
    project_dir = '/bml/CryoEM/CryoEM_Final_Dataset/' + empiar_ids[m] +  '/ground_truth'


    xyz = glob.glob(project_dir + '/particle_coordinates/*.csv')
    df = pd.read_csv(xyz[0])
    diameter = df['Diameter'].unique()

    print("EMPIAR " + empiar_ids[m] + ": Number of Particles Stack/Coordinates Files -  " + str(len(xyz)) + ' | Diameter of Particle - ' + str(diameter[0]))

