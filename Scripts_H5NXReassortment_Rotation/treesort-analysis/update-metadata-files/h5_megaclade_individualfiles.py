#! /usr/bin/env python 

#This script writes new metadata files that contain only samples/strains from one megaclade

# Define megaclade mapping using dictionary
megaclade_map = {
    "2.3.2.1s": {
        "2.3.2", "2.3.2.1", "2.3.2.1a", "2.3.2.1b", "2.3.2.1c", "2.3.2.1c-like",
        "2.3.2.1d", "2.3.2.1e", "2.3.2.1f", "2.3.2.1g"
    },
    "2.3.4.4s": {
        "2.3.3", "2.3.4", "2.3.4.1", "2.3.4.2", "2.3.4.3", "2.3.4.4",
        "2.3.4.4-like", "2.3.4.4a", "2.3.4.4c", "2.3.4.4d",
        "2.3.4.4e", "2.3.4.4f", "2.3.4.4g", "2.3.4.4h"
    },
    "2.3.4.4b": {"2.3.4.4b"},
    "Am-nonGsGD": {"Am-nonGsGD"},
    "EA-nonGsGD": {"EA-nonGsGD"},
}

#function to get the mega clade from a given clade
def get_megaclade(clade):
    clade = clade.strip()  # Clean up clade name (removes extra spaces)
    #megaclade_map.items() returns a "view" of the dictionary's key value pairs
    #for megaclade, clades in... is a tuple unpacking mechanism 
    	#on each iteraction of the loop, it extracts the key and the value into the 
    	#variables megaclade and clades
    for megaclade, clades in megaclade_map.items(): #reads the key and values iteratively
        if clade in clades:
            return megaclade
    return "other"

# File paths
InFileName = "metadata-with-clade.tsv"
OutFileName_megaclade = "metadata-with-megaclade.tsv"

# Output file handles (by megaclade)
output_files = {
    "2.3.2.1s": open("h5-clade-2321s.txt", 'w'),
    "2.3.4.4s": open("h5-clade-2344s.txt", 'w'),
    "2.3.4.4b": open("h5-clade-2344b.txt", 'w'),
    "Am-nonGsGD": open("h5-clade-AmNonGsGD.txt", 'w'),
    "EA-nonGsGD": open("h5-clade-EANonGsGD.txt", 'w'),
    "other": open("h5-clade-other.txt", 'w'),
}
OutFile_megaclade = open(OutFileName_megaclade, 'w')

# Read input and write header
with open(InFileName, 'r') as InFile:
    header = InFile.readline().strip()
    OutFile_megaclade.write(header + "\th5_megaclade\n")
    
    for line in InFile:
        line = line.strip()
        elements = line.split('\t')
        if len(elements) < 19:
            continue
        
        clade = elements[18]
        megaclade = get_megaclade(clade)
        
        # Write to the megaclade output file
        OutFile_megaclade.write(line + "\t" + megaclade + "\n")
        
        # Write to the specific clade file
        strain = elements[0]
        output_line = f"{strain}\n" #only the strain now 
        output_files[megaclade].write(output_line)

# Close all output files
OutFile_megaclade.close()
for f in output_files.values():
    f.close()

