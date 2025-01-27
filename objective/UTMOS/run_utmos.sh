#!/usr/bin/env bash

# ground truth
python predict.py --mode predict_dir --inp_dir ../../datasets/ground_truth --bs 1 --out_path results/utmos-ground_truth.csv

# tts models
for idx in {1..3}
do
  python predict.py --mode predict_dir --inp_dir ../../datasets/tts${idx} --bs 1 --out_path results/utmos-tts${idx}.csv
done