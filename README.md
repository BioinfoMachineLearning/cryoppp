# CryoPPP: A Large Expert-Labelled Cryo-EM Image Dataset for Machine Learning Protein Particle Picking 
This repository contains scripts used to crawl, process, annotate, and post procress CryoEM protein particle picking (CryoPPP) dataset.

## Data Download and Extraction 
Path to Dataset: http://calla.rnet.missouri.edu/cryoppp 

Each EMPIAR ID in CryoPPP is available as a compressed file (tar.gz) that can be downloaded by simply clicking on the file. 
Once you have downloaded the file, you must extract its contents. For example, to extract the tar file 10005.tar.gz, use command: \
`tar -zxvf 10005.tar.gz -C` 

Alternatively, if you are using a Windows operating system, you can use tools such as WinRAR or 7zip to extract the file.


## Dataset Directory Structure:

![figure_9](https://user-images.githubusercontent.com/24986485/221978450-f80fcc72-85d1-4086-9186-1c43527736a6.jpg)

CryoPPP is a diverse, open-access, high-resolution Cryo-Electron Microscopy protein dataset for single particle analysis with benchmarking ground truth annotations. It consists of manually labelled cryo-EM micrographs of 32 non-redundant, representative protein datasets selected from Electron Microscopy Public Image Archive (EMPIAR). It includes 9,089 diverse, high-resolution micrographs (~300 cryo-EM images per EMPIAR dataset) in which the coordinates of protein particles were identified by human experts. The protein particle labeling process was rigorously validated by both 2D particle class validation and 3D density map validation with the gold standard. We believe that the CryoPPP would bridge the gap between the computational potential of Deep Learning and the standard benchmarking dataset inadequacy for high-end microscopic analysis of Cryo-EM micrographs in academic research. 

## Data Curation and Ground Truth Annotation Procedure:

![Picture2](https://user-images.githubusercontent.com/24986485/219126688-016db1be-f6d0-427b-87b6-aecc25c43f28.jpg)

## Data Records

The CryoPPP dataset consists of 32 ground truth data and metadata for 335 EMPIAR IDs. The ground truth data is comprised of variety of 9089 Micrographs (~300 cryo-EM images per EMPIAR ID) with manually curated ground truth coordinates of picked protein particles. The metadata consists of 1,698,802 high resolution micrographs deposited in EMPIAR with their respective FPT and Globus data download paths. Link to Cryo-EM protein Metadata: http://calla.rnet.missouri.edu/cryoppp/EMPIAR_metadata_335.xlsx

## Example Dataset
![readme_git](https://user-images.githubusercontent.com/24986485/221383343-8ddec678-52e9-467b-a0d5-4f76b9b3f4e0.jpg)


Each data folder (titled after the corresponding EMPIAR dataset ID) for all expert labelled data includes the following information: raw micrographs / motion corrected micrographs, gain motion correction file, ground truth, and particles stack. 


## CryoPPP Statistics
Statistics of true protein particles for each EMPIAR database in CryoPPP: 

| SN | EMPAIR ID | Protein Type                      | Number of Micrographs | Image size   | Particle Diameter (A) | Number of True Protein Particles |
| -- | --------- | --------------------------------- | --------------------- | ------------ | --------------------- | -------------------------------- |
| 1  | 10389     | Metal Binding Protein             | 300                   | (3838, 3710) | 200                   | 10870                            |
| 2  | 10081     | Transport Protein                 | 300                   | (3710, 3838) | 200                   | 39352                            |
| 3  | 10289     | Transport Protein                 | 300                   | (3710, 3838) | 200                   | 61517                            |
| 4  | 11057     | Hydrolase                         | 300                   | (5760, 4092) | 140                   | 45219                            |
| 5  | 10444     | Membrane Protein                  | 300                   | (5760, 4092) | 180                   | 58731                            |
| 6  | 10576     | Nuclear Protein (DNA)             | 295                   | (7420, 7676) | 180                   | 75220                            |
| 7  | 10816     | Transport Protein                 | 300                   | (7676, 7420) | 180                   | 45363                            |
| 8  | 10526     | Ribosome (50S)                    | 294                   | (7676, 7420) | 400                   | 3265                             |
| 9  | 11051     | Transcription/DNA/RNA             | 300                   | (3838, 3710) | 180                   | 83227                            |
| 10 | 10760     | Membrane Protein                  | 300                   | (3838, 3710) | 130                   | 173664                           |
| 11 | 11183     | Signaling Protein                 | 300                   | (5760, 4092) | 140                   | 80014                            |
| 12 | 10671     | Signaling Protein                 | 298                   | (5760, 4092) | 110                   | 69012                            |
| 13 | 10291     | Transport Protein                 | 300                   | (3710, 3838) | 160                   | 99808                            |
| 14 | 10669     | Proteasome (Plant Protein)        | 300                   | (7676, 7420) | 500                   | 19660                            |
| 15 | 10077     | Ribosome (70S)                    | 300                   | (4096, 4096) | 250                   | 31919                            |
| 16 | 10061     | Hydrolase (Beta-galactosidase)    | 300                   | (7676, 7420) | 150                   | 35218                            |
| 17 | 10097     | Viral Protein                     | 300                   | (3838, 3710) | 140                   | 58629                            |
| 18 | 10028     | Ribosome (80S)                    | 300                   | (4096, 4096) | 300                   | 26391                            |
| 19 | 10096     | Viral Protein                     | 300                   | (3838, 3710) | 110                   | 231351                           |
| 20 | 10737     | Membrane Protein (E-coli)         | 293                   | (5760, 4092) | 179                   | 59265                            |
| 21 | 10387     | Protein + DNA                     | 300                   | (3710, 3838) | 168                   | 101778                           |
| 22 | 10532     | VIRAL PROTEIN                     | 300                   | (4096, 4096) | 179                   | 87933                            |
| 23 | 10240     | LIPD TRANSPORT                    | 300                   | (3838, 3710) | 170                   | 85958                            |
| 24 | 10005     | TRPV1 Tansport protein            | 30                    | (3710, 3710) | 172                   | 5374                             |
| 25 | 10017     | β -galactosidase                  | 84                    | (4096, 4096) | 190                   | 49391                            |
| 26 | 10075     | Bacteriophage MS2                 | 300                   | (4096, 4096) | 270                   | 12682                            |
| 27 | 10184     | Aldolase                          | 300                   | (3838, 3710) | 100                   | 219849                           |
| 28 | 10059     | TRPV1                             | 295                   | (3838, 3710) | 160                   | 190398                           |
| 29 | 10406     | 70S Ribosome                      | 300                   | (3838, 3710) | 226                   | 24703                            |
| 30 | 10590     | TRPV1 with DkTx and RTX           | 300                   | (3710, 3838) | 236                   | 62493                            |
| 31 | 10093     | Mechanotransduction channel NOMPC | 300                   | (3838, 3710) | 208                   | 56394                            |
| 32 | 10345     | Signaling Protein                 | 300                   | (3710, 3838) | 200                   | 15894                            |

## Data Usage for ML-Based Applications:

Researchers can use CryoPPP to train and test their Machine Learning / Deep Learning based methods for automated cryo-EM protein particle picking. 

Users are supposed to use motion corrected 2D images (micrographs) as input. The protein particle's coordinate information for corresponding micrographs are located inside 'ground_truth' >>
'particle_coordinates' folder. The file naming convention for both the micrographs and their corresponding particle's coordinate are same for user's ease. 

###Example: 
For EMPIAR 10005, the motion corrected micrograph is: 10005>>micrographs>>stack_0002_2x_SumCorr.mrc 
and the corresponding particle's coordinate information is found here: 10005>>ground_truth>>particle_coordinates>>stack_0002_2x_SumCorr.csv

The particle stack is: 10005>>particles_stack>>stack_0002_2x_SumCorr_particles.mrc 
and the corresponding star file for all protein particles in EMPIAR 10005 is store as .star file in: 10005>>ground_truth>>empiar-10005_particles_selected.star 


-----

## Rights and Permissions
Open Access \
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.


** Link to CryoPPP paper ** : https://www.biorxiv.org/content/10.1101/2023.02.21.529443v1

## Cite this work
If you use the code or data associated with this research work or otherwise find this data useful, please cite: \
@article {Dhakal2023.02.21.529443, \
	author = {Dhakal, Ashwin and Gyawali, Rajan and Wang, Liguo and Cheng, Jianlin}, \
	title = {CryoPPP: A Large Expert-Labelled Cryo-EM Image Dataset for Machine Learning Protein Particle Picking}, \
	elocation-id = {2023.02.21.529443}, \
	year = {2023}, \
	doi = {10.1101/2023.02.21.529443}, \
	journal = {bioRxiv} \
}
