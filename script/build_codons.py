#!/usr/bin/python3

# ask about AGA, AGG being 4/3 and not 2/3 (is every change == 1/3???)
CodonDict = {
    "ATG":[0, "M"], "TGG":[0, "W"], "ACT":[1, "T"], "ACC":[1, "T"], "ACA":[1, "T"], "ACG":[1, "T"], "TCT":[1, "S"], 
    "TCC":[1, "S"], "TCA":[1, "S"], "TCG":[1, "S"], "CTT":[1, "L"], "CTA":[1, "L"], "CTC":[1, "L"], "CTG":[1, "L"],
    "CCT":[1, "P"], "CCA":[1, "P"], "CCC":[1, "P"], "CCG":[1, "P"], "CGT":[1, "R"], "CGC":[1, "R"], "GTT":[1, "V"],
    "GTC":[1, "V"], "GTA":[1, "V"], "GTC":[1, "V"], "GTG":[1, "V"], "GCT":[1, "A"], "GCA":[1, "A"], "GCC":[1, "A"], 
    "GCG":[1, "A"], "GGT":[1, "G"], "GGC":[1, "G"], "GGA":[1, "G"], "GGG":[1, "G"], 
    "AAT":[1/3, "N"], "AAC":[1/3, "N"], "AAA":[1/3, "K"], "AAG":[1/3, "K"], "AGT":[1/3, "S"], "AGC":[1/3, "S"], "TTT":[1/3, "F"],
    "TTC":[1/3, "F"], "TAT":[1/3, "Y"], "TAC":[1/3, "Y"], "TGT":[1/3, "C"], "TGC":[1/3, "C"], "TGA":[1/3, "X"], "CAT":[1/3, "H"], 
    "CAC":[1/3, "H"], "CAA":[1/3, "Q"], "CAG":[1/3, "Q"], "GAT":[1/3, "D"], "GAA":[1/3, "E"], "GAC":[1/3, "D"], "GAG":[1/3, "E"], 
    "ATT":[2/3, "I"], "ATC":[2/3, "I"], "ATA":[2/3, "I"], "AGA":[2/3, "R"], "AGG":[2/3, "R"], "TTA":[2/3, "L"], "TTG":[2/3, "L"], 
    "TAA":[2/3, "X"], "TAG":[2/3, "X"], "CGA":[4/3, "R"], "CGG":[4/3, "R"]}

with open("/mnt/c/Users/pfoth/OneDrive/Desktop/leslie_project/Mapourika_Histones/MP2_R1.fastq.Histone_H2A_wo_header.raw", "r") as raw_file:
    dna_sequence = ""
    for line in raw_file:
        line = line.split()
        dna_sequence += line[3]
    i = 0
    codon_list = []
    one_letter_aa_code = ""
    while (i < len(dna_sequence)):
        current_codon = ""
        for x in range(3):
            nucleotide_position = i + x
            current_codon += dna_sequence[nucleotide_position]
        info = [current_codon, CodonDict[current_codon][1], CodonDict[current_codon][0]]
        codon_list.append(info)
        i += 3

print(codon_list)
