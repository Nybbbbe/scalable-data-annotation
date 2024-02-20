module load miniconda

conda create -n jancv39 python=3.9

source activate jancv39

conda info

pip3 install --user -r requirements.txt

python3 train-cifar.py --dataset "cifar100" --n-lbl 4000 --class-blnc 1 --split-txt "run1" --arch "cnn13"

srun -t 08:00:00 --mem=8G --gres=gpu:v100:1 -o ups3.log -e error3.log --mail-user=jan.nyberg@gmail.com python3 train-cifar.py --dataset "cifar10" --n-lbl 1000 --class-blnc 7 --split-txt "run1" --arch "cnn13"


squeue --me