#!/bin/bash
######################################## BSUB Headers ###########################################
#BSUB -J job-name-test
#BSUB -P BIF135-TWO
#BSUB -W 24:00
#BSUB -nnodes 1
#BSUB -q batch-hm
#BSUB -o file-name%J.out
#BSUB -e file-name%J.error
#################################################################################################
# Remote project path and DGL backend override
module load open-ce
conda activate CryoEm
jsrun -g1 -a1 -c42 -r1 python copy_microimage_files.py
