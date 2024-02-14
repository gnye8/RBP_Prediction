import os
import argparse
import pandas as pd
import arnie
from arnie.bpps import bpps
from Bio import SeqIO
import json 
import numpy as np

def spawn_child_job(seqs, indexes, IDs, idx, template_sbatch, outputs_folder, eternafold_preds_script):
    os.system(f'cp {template_sbatch} {outputs_folder}/{idx}.sbatch')
    child_df = pd.DataFrame(zip(indexes, IDs, seqs), columns=['index', 'ID', 'seq'])
    child_df.to_csv(f'{args.outputs_folder}/child{idx}.csv')

    with open(f'{outputs_folder}/{idx}.sbatch', 'a') as file:
        lines = []
        lines.append(f'python {eternafold_preds_script} --child_dataframe {outputs_folder}/child{idx}.csv --outputs_folder {outputs_folder}')
        file.writelines(lines)

    os.system(f'sbatch {outputs_folder}/{idx}.sbatch')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--dataframe', required=True)
    parser.add_argument('--outputs_folder', required=True)
    parser.add_argument('--template_sbatch', required=True)
    parser.add_argument('--eternafold_preds_script', default='/scratch/groups/rhiju/gnye8/RBP_binding/scripts/eternafold_preds.py')
    args=parser.parse_args()

    df = pd.read_csv(args.dataframe, index_col=0)
    index_to_predict = []
    IDs_to_predict = []
    #windows_to_predict_window_num = []
    seqs_to_predict = []
    for index,row in df.iterrows():
        seq = row['padded_seqs'].strip('n')
        seqs_to_predict.append(seq)
        IDs_to_predict.append(row['ID'])
        index_to_predict.append(index)

        #for i in range(0, 301, 50):
            #print(i)
            #window = row[f'window{i}'].strip('n')
            #if len(window) > 0:
                #windows_to_predict_index.append(index)
                #windows_to_predict_ID.append(row['ID'])
                #windows_to_predict_window_num.append(f'window{i}')
                #windows_to_predict_seqs.append(window)

    for i in range(0, len(seqs_to_predict)+1, round(len(seqs_to_predict) / 900)):
        child_job_seqs = seqs_to_predict[i:i+round(len(seqs_to_predict) / 900)]
        child_job_indexes = index_to_predict[i:i+round(len(index_to_predict) / 900)]
        child_job_IDs = IDs_to_predict[i:i+round(len(IDs_to_predict) / 900)]
        #child_job_window_nums = windows_to_predict_window_num[i:i+round(len(windows_to_predict_window_num) / 900)]

        spawn_child_job(child_job_seqs, child_job_indexes, child_job_IDs, idx=i, template_sbatch=args.template_sbatch, outputs_folder=args.outputs_folder, eternafold_preds_script=args.eternafold_preds_script)

