# CryoPPP: A Large Expert-Curated Cryo-EM Image Dataset for Machine Learning Protein Particle Picking 
This repository contains scripts used to crawl, download, process, annotate, and post procress the CryoEM protein particle picking (CryoPPP) dataset.

## Data Download and Extraction in one of the three ways

## Option 1: Direct download all data from our server

Path to CryoPPP Dataset: http://calla.rnet.missouri.edu/cryoppp 

Each EMPIAR ID in CryoPPP is available as a compressed file (tar.gz) that can be downloaded by simply clicking on the file. Once you have downloaded the file, you must extract its contents. If you are using a Windows operating system, you can use tools such as WinRAR or 7zip to extract the file. \
OR \
To download and extract dataset (ex: 10005), use command: \
`wget https://calla.rnet.missouri.edu/cryoppp/10005.tar.gz` \
`tar -zxvf 10005.tar.gz -C` 


## Option 2: Use scripts to download all the cryo-EM micrographs from EMPIAR and labels from Zenodo
`git clone https://github.com/BioinfoMachineLearning/cryoppp.git` \
`cd download_micrographs_motion_correction_files` \
`python downloading_micrographs_from_EMPIAR.py` 

These commands will enable you to download micrographs and all of the required motion correction files. Next, you should retrieve the protein particle labels from Zenodo by accessing this link: https://zenodo.org/record/7934683


## Option 3: Download a light version of the data where there is only limited disk space
If storage space is a concern, researchers can opt for a more lightweight version of CryoPPP called CryoPPP_Lite.  
CryoPPP_Lite includes truncated versions of the original micrographs and particle ground truth files that result in a total storage size of 121 GB, making it easier to store and transfer. This version includes an 8-bit representation of micrographs in JPG format, along with the necessary particle coordinate files for 34 Cryo-EM datasets.

Path to CryoPPP_Lite Dataset: http://calla.rnet.missouri.edu/cryoppp_lite \
The steps to download and extract the data files are identical to the instructions provided in option 1.


## CryoPPP Dataset Directory Structure:

![figure_9](https://github.com/BioinfoMachineLearning/cryoppp/assets/24986485/04f4b35c-70c0-4ccd-8f9d-67b33063b2f7)

CryoPPP is a large, diverse, expert-curated cryo-EM image dataset for protein particle picking and analysis. It consists of labelled cryo-EM micrographs of 34 representative protein datasets selected from Electron Microscopy Public Image Archive (EMPIAR). The dataset is 2.6 terabytes and includes 9,893 high-resolution micrographs with labelled protein particle coordinates. The labelling process was rigorously validated through 2D particle class validation and 3D density map validation with the gold standard. The dataset is expected to greatly facilitate the development of AI-based and classical methods for automated cryo-EM protein particle picking. 

## Data Curation and Ground Truth Annotation Procedure:

![Picture2](https://user-images.githubusercontent.com/24986485/219126688-016db1be-f6d0-427b-87b6-aecc25c43f28.jpg)

## Data Records

The CryoPPP dataset consists of 34 ground truth data and metadata for 335 EMPIAR IDs. The ground truth data is comprised of variety of 9893 Micrographs (~300 cryo-EM images per EMPIAR ID) with manually curated ground truth coordinates of picked protein particles. The metadata consists of 1,698,802 high resolution micrographs deposited in EMPIAR with their respective FPT and Globus data download paths. Link to Cryo-EM protein Metadata: http://calla.rnet.missouri.edu/cryoppp/EMPIAR_metadata_335.xlsx

## Example Dataset
![readme_git](https://user-images.githubusercontent.com/24986485/221383343-8ddec678-52e9-467b-a0d5-4f76b9b3f4e0.jpg)


Each data folder (titled after the corresponding EMPIAR dataset ID) for all expert labelled data includes the following information: raw micrographs / motion corrected micrographs, gain motion correction file, ground truth, and particles stack. 


## CryoPPP Statistics
Statistics of true protein particles for each EMPIAR database in CryoPPP: 

| **SN** | **EMPAIR ID** | **Protein Type**               | **Size (TB)** | **Number of Micrographs** | **Image size** | **Particle Diameter (px)** | **Total Structure Weight (kDa)** | **Number of True Protein Particles** |
| ------ | ------------- | ------------------------------ | ------------- | ------------------------- | -------------- | -------------------------- | -------------------------------- | ------------------------------------ |
| 1      | 10389         | Metal Binding Protein          | 0.224         | 300                       | (3838, 3710)   | 313                        | 1042.17                          | 10870                                |
| 2      | 10081         | Transport Protein              | 0.052         | 300                       | (3710, 3838)   | 154                        | 298.57                           | 39352                                |
| 3      | 10289         | Transport Protein              | 0.048         | 300                       | (3710, 3838)   | 162                        | 361.39                           | 61517                                |
| 4      | 11057         | Hydrolase                      | 2.100         | 300                       | (5760, 4092)   | 186                        | 149.43                           | 45219                                |
| 5      | 10444         | Membrane Protein               | 2.399         | 300                       | (5760, 4092)   | 217                        | 295.89                           | 58731                                |
| 6      | 10576         | Nuclear Protein (DNA)          | 0.722         | 295                       | (7420, 7676)   | 265                        | 290.21                           | 75220                                |
| 7      | 10816         | Transport Protein              | 1.500         | 300                       | (7676, 7420)   | 359                        | 166.62                           | 45363                                |
| 8      | 10526         | Ribosome (50S)                 | 0.460         | 294                       | (7676, 7420)   | 482                        | 1085.81                          | 3265                                 |
| 9      | 11051         | Transcription/DNA/RNA          | 2.300         | 300                       | (3838, 3710)   | 214                        | 357.31                           | 83227                                |
| 10     | 10760         | Membrane Protein               | 0.199         | 300                       | (3838, 3710)   | 106                        | 321.69                           | 173664                               |
| 11     | 11183         | Signaling Protein              | 0.326         | 300                       | (5760, 4092)   | 159                        | 139.36                           | 80014                                |
| 12     | 10671         | Signaling Protein              | 1.600         | 298                       | (5760, 4092)   | 133                        | 77.14                            | 69012                                |
| 13     | 10291         | Transport Protein              | 0.016         | 300                       | (3710, 3838)   | 130                        | 361.39                           | 99808                                |
| 14     | 10669         | Proteasome (Plant Protein)     | 13.899        | 300                       | (7676, 7420)   | 730                        | 1681.81                          | 19660                                |
| 15     | 10077         | Ribosome (70S)                 | 0.774         | 300                       | (4096, 4096)   | 216                        | 2198.78                          | 31919                                |
| 16     | 10061         | Hydrolase (Beta-galactosidase) | 0.319         | 300                       | (7676, 7420)   | 471                        | 467.06                           | 35218                                |
| 17     | 10028         | Ribosome (80S)                 | 1.100         | 300                       | (4096, 4096)   | 224                        | 2135.89                          | 26391                                |
| 18     | 10096         | Viral Protein                  | 1.199         | 300                       | (3838, 3710)   | 84                         | 150\*                            | 231351                               |
| 19     | 10737         | Membrane Protein (E-coli)      | 0.831         | 293                       | (5760, 4092)   | 179                        | 155.83                           | 59265                                |
| 20     | 10387         | Viral Protein (DNA)            | 0.105         | 300                       | (3710, 3838)   | 213                        | 185.87                           | 101778                               |
| 21     | 10532         | Viral Protein                  | 0.196         | 300                       | (4096, 4096)   | 174                        | 191.76                           | 87933                                |
| 22     | 10240         | Lipid Transport Protein        | 0.111         | 300                       | (3838, 3710)   | 156                        | 171.72                           | 85958                                |
| 23     | 10005         | TRPV1 Transport protein        | 0.044         | 30                        | (3710, 3710)   | 142                        | 272.97                           | 5374                                 |
| 24     | 10017         | β -galactosidase               | 0.005         | 84                        | (4096, 4096)   | 108                        | 450\*                            | 49391                                |
| 25     | 10075         | Bacteriophage MS2              | 0.046         | 300                       | (4096, 4096)   | 233                        | 1000\*                           | 12682                                |
| 26     | 10184         | Aldolase                       | 0.084         | 300                       | (3838, 3710)   | 118                        | 150\*                            | 219849                               |
| 27     | 10059         | Transport Protein (TRPV1)      | 0.062         | 295                       | (3838, 3710)   | 132                        | 317.88                           | 190398                               |
| 28     | 10406         | Ribosome (70S)                 | 0.141         | 300                       | (3838, 3710)   | 212                        | 632.89                           | 24703                                |
| 29     | 10590         | TRPV1 with DkTx and RTX        | 0.252         | 300                       | (3710, 3838)   | 158                        | 1000\*                           | 62493                                |
| 30     | 10093         | Membrane Protein               | 0.097         | 300                       | (3838, 3710)   | 172                        | 779.4                            | 56394                                |
| 31     | 10345         | Signaling Protein              | 0.085         | 300                       | (3838, 3710)   | 149                        | 244.68                           | 15894                                |
| 32     | 11056         | Transport Protein              | 0.164         | 361                       | (5760, 4092)   | 164                        | 88.94                            | 125908                               |
| 33     | 10852         | Signaling Protein              | 0.227         | 343                       | (5760, 4092)   | 123                        | 157.81                           | 310291                               |
| 34     | 10947         | Viral Protein                  | 0.048         | 400                       | (4096, 4096)   | 240                        | 443.92                           | 106393                               |

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
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.


** Link to CryoPPP paper ** : https://www.nature.com/articles/s41597-023-02280-2

## Cite this work
If you use the code or data associated with this research work or otherwise find this data useful, please cite: \
@article {Dhakal2023, \
	author = {Dhakal, Ashwin and Gyawali, Rajan and Wang, Liguo and Cheng, Jianlin}, \
	title = {A large expert-curated cryo-EM image dataset for machine learning protein particle picking}, \
	year = {2023}, \
    volume = {10}, \
    issue = {1}, \
	doi = {10.1038/s41597-023-02280-2}, \
	journal = {Scientific Data}, \
    url = {https://doi.org/10.1038/s41597-023-02280-2}
}
