#!/usr/bin/env python
# coding: utf-8

#similar to fasta_to_df? 


# In[ ]:


import pandas as pd
import os

def fasta_to_df(fasta_file):
    
    fasta_data = []
    
    with open(fasta_file) as f:
        header = ""
        sequence = ""
        for line in f:
            if line.startswith(">"):
                if header != "":
                    fasta_data.append({"header": header, "sequence": sequence})
                header = line.strip() 
                sequence = ""
            else:
                sequence += line.strip()
        fasta_data.append({"header": header, "sequence": sequence}) #last line
            
    return pd.DataFrame(fasta_data)

def fasta_writer(path, filename, df):

    #os.mkdir(path) attempts to create the directory specified by path.
# 	If the directory already exists or can't be created, the except block catches the error and simply does nothing (pass).
# 	This is a simple way to ensure the target directory exists without crashing the program if it doesn't need to be created.
    try:  
        os.mkdir(path)

    except OSError as error:
        pass

    with open(f"{path}{filename}", "w") as f:
        for index, row in df.iterrows():
            f.write(f"{row['header']}\n")
            f.write(f"{row['sequence']}\n")

# Opens (or creates) a file at the full path {path}{filename} in write mode ("w").
# Iterates over each row in the DataFrame df.
# For each row:
# Writes the value in the 'header' column followed by a newline.
# Writes the value in the 'sequence' column followed by a newline.
# This structure corresponds to the FASTA file format, where each record has:
# A header line starting with > (assumed to be included in row['header'])
# A sequence line (nucleotide or protein sequence)
