#!/bin/bash
#SBATCH --job-name=summarize    # Job name
#SBATCH --output=summarize.out   # Standard output
#SBATCH --error=summarize.err     # Standard error
#SBATCH --ntasks=1                  # Run a single task
#SBATCH --cpus-per-task=10          # Number of CPU cores per task
#SBATCH --partition=cpu-killable               
#SBATCH --nodelist=rack-iscb-31

python3 summarize.py ../filtered_q2_2023_news.csv