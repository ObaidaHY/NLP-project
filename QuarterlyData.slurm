#!/bin/bash
#SBATCH --job-name=fastQuart    # Job name
#SBATCH --output=output_%A_%a.out   # Standard output
#SBATCH --error=error_%A_%a.err     # Standard error
#SBATCH --ntasks=1                  # Run a single task
#SBATCH --cpus-per-task=16           # Number of CPU cores per task
#SBATCH --partition=cpu-killable               
#SBATCH --nodelist=rack-ai-01


python QuarterlyFast.py --year $YEAR --quarter $QUARTER
