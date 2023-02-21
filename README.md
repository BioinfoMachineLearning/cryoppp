# CryoPPP: A Large Expert-Curated Cryo-Electron Microscopy Image Dataset for Single Particle Picking 
This repository contains scripts used to crawl, download, process and annotate CryoEM protein particle data with ground truth annotations.

## Path to Dataset:
http://calla.rnet.missouri.edu/cryoEM_particle_data/

## Dataset Directory Structure:

![direc](https://user-images.githubusercontent.com/24986485/214904761-94030d5e-ff8a-4286-a2d5-e6c2466195e0.jpg)


‘CryoPPP’ is a diverse, open-access, high-resolution Cryo-Electron Microscopy protein dataset for single particle analysis with benchmarking ground truth annotations. It consists of 335 EMPIAR ID’s metadata and 32 EMPIAR IDs with ground truth annotations. The metadata consists of 1,698,802 high resolution (<4 A) micrographs deposited in Electron Microscopy Public Image Archive (EMPIAR) with their corresponding FPT and Globus data download links. Moreover, 32 ground truth data consist of diversified 9089 Micrographs (~300 Cryo-EM images per EMPIAR ID) with manually curated ground truth coordinate of picked protein particles. We believe that the Cryo-PDS would bridge the gap between the computational potential of Deep Learning and the standard benchmarking dataset inadequacy for high-end microscopic analysis of Cryo-EM micrographs in academic research. 

## Data Curation and Ground Truth Annotation Procedure:

![Picture2](https://user-images.githubusercontent.com/24986485/219126688-016db1be-f6d0-427b-87b6-aecc25c43f28.jpg)

## Data Records

The CryoPPP dataset consists of 32 ground truth data and metadata for 335 EMPIAR IDs. The ground truth data is comprised of variety of 9089 Micrographs (~300 cryo-EM images per EMPIAR ID) with manually curated ground truth coordinates of picked protein particles. The metadata consists of 1,698,802 high resolution micrographs deposited in EMPIAR with their respective FPT and Globus data download paths.

Each data folder (titled after the corresponding EMPIAR ID) for all ground truth annotated data includes the following information: raw micrographs, gain motion correction file, ground truth, and particles stack. Please refer to the paper for entire dataset directory.

Link to Cryo-PDS paper: 
