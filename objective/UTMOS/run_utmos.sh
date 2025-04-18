#!/usr/bin/env

# ground truth
python predict.py --mode predict_dir --inp_dir ../dataset/ground_truth --bs 1 --out_path ..results/utmos_ground_truth.csv

# tts models
for idx in {1..3}
do
  python predict.py --mode predict_dir --inp_dir ../dataset/tts${idx} --bs 1 --out_path ..results/utmos_tts${idx}.csv
done