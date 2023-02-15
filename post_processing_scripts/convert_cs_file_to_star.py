#!/usr/bin/env python
# coding: utf-8

# # Install pyem on your machine

# ## Create a new conda environment and install the dependencies



#Run these commands
get_ipython().system('conda create -n pyem')
get_ipython().system('conda activate pyem')
get_ipython().system('conda install numpy scipy matplotlib seaborn numba pandas natsort')
get_ipython().system('conda install -c conda-forge pyfftw healpy pathos')


# ## Install pyem



# Clone this repository to /home/*/Documents/
# Run these commands by staying in /home/*/Documents/
get_ipython().system('mkdir Results')
get_ipython().system('git clone https://github.com/asarnow/pyem.git')
get_ipython().system('cd pyem')
get_ipython().system('pip install --no-dependencies -e .')
get_ipython().system('pip install jupyter')


# # Run the Script 


#Start Terminal
# activate the pyem environment by using " conda activate pyem "
# Run " jupyter notebook "
# Open this notebook file from jupyter notebook




import glob
import os
import subprocess

#Change this according to your structure of Cryo EM project directory

project_dir = '/home/*/*/CryoEMData/'


dirs = glob.glob(project_dir + '*/CS-empiar*/exports/groups/*/*_particles_*.cs') #Replace front * by empiar-id directory(eg: 11111)
                                                            #  if, you want to convert project by project
for dir in dirs:
    empiar_id = dir.split('/')[-5][3:]
    filename_cs = dir.split('/')[-1]
    filename = filename_cs[:-3]
    filename = filename.split('_')[1] + "_" + filename.split('_')[2]
    filename_star = empiar_id + '_' + filename + '.star'
    directory = dir.replace(filename_cs, '')
    cmd  = "python pyem/csparc2star.py " + dir + " " + directory + filename_star
    print(cmd)
    print("\n")
    subprocess.call(cmd, shell=True)



