#!/bin/bash
#SBATCH --job-name=ups
#SBATCH --time=00:15:00
#SBATCH --mem=8G
#SBATCH --output=output%j.txt
#SBATCH --gres=gpu:1

srun python3 ups/train-cifar.py --dataset "cifar10" --n-lbl 1000 --class-blnc 7 --split-txt "run1" --arch "cnn13"