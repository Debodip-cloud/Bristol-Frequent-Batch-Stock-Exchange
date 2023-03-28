#!/bin/bash

#SBATCH --job-name BFBSE
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 1
#SBATCH --time 03:00:00
#SBATCH --cpus-per-task=2
#SBATCH --partition=teach_cpu
#SBATCH --account=COSC028844

python csv_generator.py
python tbse.py test_combinations.csv
python my_analysis.py
python plotter_results.py
