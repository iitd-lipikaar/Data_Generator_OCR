#!/bin/bash

# Synth DATA (Bengali, Punjabi, Tamil, Hindi, Telugu)

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_bengali" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_bengali/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang5/train/synth/st_bn" --num_processes=24

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_punjabi" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_punjabi/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang5/train/synth/st_pb" --num_processes=24

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_tamil" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_tamil/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang5/train/synth/st_tm" --num_processes=24

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_hindi" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_hindi/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang5/train/synth/st_hi" --num_processes=24

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_telugu" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results/output_telugu/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang5/train/synth/st_te" --num_processes=24



# Synth DATA (Assamese, gujarati, malayalam, manipuri, oriya, Kannada)

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_10/output_assamese" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_10/output_assamese/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/train/synth/st_10_as" --num_processes=24

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_val/output_gujarati" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_val/output_gujarati/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/val/st_val_gj" --num_processes=24

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_new/output_manipuri" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_new/output_manipuri/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/train/synth/st_10_mn" --num_processes=24

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_new/output_malayalam" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_new/output_malayalam/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/train/synth/st_10_ml" --num_processes=24

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_val/output_oriya" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_val/output_oriya/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/val/st_val_or" --num_processes=24

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_val/output_kannada" --Input_gtFile "/home/scai/mtech/aib232080/scratch/synthtiger_2/results_val/output_kannada/gt.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/val/st_val_kn" --num_processes=24