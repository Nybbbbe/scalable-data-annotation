#!/bin/bash
#SBATCH --job-name=experiment1
#SBATCH --time=00:10:00
#SBATCH --mem=1G
#SBATCH --output=output/output%j.txt
#SBATCH --error=errors/error%j.txt