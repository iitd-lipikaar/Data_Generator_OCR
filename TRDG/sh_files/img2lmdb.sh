#!/bin/bash


# TRDG DATA (Bengali, Punjabi, Tamil, Hindi, Telugu)

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_bengali" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_bengali/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang6/train/synth/trdg_bn" --num_processes=55

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_punjabi" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_punjabi/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang6/train/synth/trdg_pb" --num_processes=55

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_tamil" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_tamil/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang6/train/synth/trdg_tm" --num_processes=55

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_hindi" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_hindi/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang6/train/synth/trdg_hi" --num_processes=55

python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_telugu" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result/output_telugu/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang6/train/synth/trdg_te" --num_processes=55

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_kannada" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_kannada/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_data/lmdb_lang7/train/synth/trdg_10_kn" --num_processes=55



# TRDG DATA (Assamese, gujarati, malayalam, manipuri, oriya, Kannada)

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_assamese" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_assamese/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/train/synth/trdg_10_as" --num_processes=55

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result_val/output_gujarati" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result_val/output_gujarati/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/val/trdg_val_gj" --num_processes=55

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_malayalam" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_malayalam/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/train/synth/trdg_10_ml" --num_processes=55

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_manipuri" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result_10/output_manipuri/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/train/synth/trdg_10_mn" --num_processes=55

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result_val/output_oriya" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result_val/output_oriya/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/val/trdg_val_or" --num_processes=55

# python img_lmdb.py --Input_ImageFolder "/home/scai/mtech/aib232080/scratch/trdg_2/result_val/output_kannada" --Input_gtFile "/home/scai/mtech/aib232080/scratch/trdg_2/result_val/output_kannada/images_trdg_labels.txt" --outputPath "/home/scai/mtech/aib232080/scratch/lmdb_lang8/val/trdg_val_kn" --num_processes=55
