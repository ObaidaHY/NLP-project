#!/bin/bash

#SBATCH --job-name=tuneFinBert             
#SBATCH --nodes=1                                 
#SBATCH --partition=killable 
#SBATCH --nodelist=n-80[1-4]
#SBATCH --gpus=1
#SBATCH --ntasks-per-node=1                       
#SBATCH --output=tuneFinBert.out         
#SBATCH --error=tuneFinBert.err  

python3 tuneFinBert.py