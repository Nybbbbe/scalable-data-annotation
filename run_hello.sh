#!/bin/bash
#SBATCH --job-name=experiment1
#SBATCH --time=00:15:00
#SBATCH --mem=1G
#SBATCH --output=output%j.txt
#SBATCH --error=error%j.txt
#SBATCH --gres=gpu:1

srun python3 test.py