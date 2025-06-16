#! /usr/bin/env python 

#made more efficient by chatgpt
#This script is meant to write new metadata files where: 
#1 we add an extra column "h5_megaclade" to the metadata file (to categorize current
#clades into larger clade groups)
#2 individual metadata file for each megaclade

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
    for megaclade, clades in megaclade_map.items(): 
        if clade in clades:
            return megaclade
    return "other"

# File paths
InFileName = "data/metadata-with-megaclade-updateddates.tsv"
OutFileName_megaclade = "metadata-with-megaclade.tsv"

# Output file handles (by megaclade)
output_files = {
    "2.3.2.1s": open("metadata-h5-clade-2321s.tsv", 'w'),
    "2.3.4.4s": open("metadata-h5-clade-2344s.tsv", 'w'),
    "2.3.4.4b": open("metadata-h5-clade-2344b.tsv", 'w'),
    "Am-nonGsGD": open("metadata-h5-clade-AmNonGsGD.tsv", 'w'),
    "EA-nonGsGD": open("metadata-h5-clade-EANonGsGD.tsv", 'w'),
    "other": open("metadata-h5-clade-other.tsv", 'w'),
}
OutFile_megaclade = open(OutFileName_megaclade, 'w')

# Read input and write header
with open(InFileName, 'r') as InFile:
    header = InFile.readline().strip()
    OutFile_megaclade.write(header + "\th5_megaclade\n")
    
    # Add headers to all specific clade output files
    for f in output_files.values():
        f.write(header + "\th5_megaclade\n")

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
        strain = elements
        output_files[megaclade].write(line + "\t" + megaclade + "\n")

# Close all output files
OutFile_megaclade.close()
for f in output_files.values():
    f.close()
