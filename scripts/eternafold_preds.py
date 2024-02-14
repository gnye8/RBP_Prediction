import os
import argparse
import pandas as pd
import arnie
from arnie.bpps import bpps
from Bio import SeqIO
import json 
import numpy as np


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--child_dataframe', required=True)
    parser.add_argument('--outputs_folder', required=True)
    args=parser.parse_args()

    child_df = pd.read_csv(f'{args.child_dataframe}', index_col=0)
    base_pairing_dict = {}
    for index,row in child_df.iterrows():
    	window_dict = {}
    	seq = row['seq']

    	bp_matrix = bpps(seq, package='eternafold')
    	p_net_base_pairing = np.sum(bp_matrix, axis=0)

    	window_dict['sequence'] = seq
    	#window_dict['index'] = row['index']
    	#window_dict['ID'] = row['ID']
    	#window_dict['window_num'] = row['window_num']
    	window_dict['p_net_base_pairing'] = list(p_net_base_pairing)
    	
    	base_pairing_dict[row['ID']] = window_dict

    save_file = open(f'{args.child_dataframe[:-4]}.json', 'w')
    json.dump(base_pairing_dict, save_file, indent=6)
    save_file.close()


