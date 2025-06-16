#! /usr/bin/env python 

#change a fasta file into a dataframe (sent to me from Maria)
#we wanted to do this so that we could look for nonnucleotides in the sequences

def fasta_to_df(path_to_fasta):
    FASTANAME = path_to_fasta
    fasta_data = []
    with open(FASTANAME) as f:
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
    fasta_df = pd.DataFrame(fasta_data)
    return(fasta_df)
    
def qc(fas)