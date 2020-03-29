#!/usr/bin/python3

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


def run_codon(codon_list, orig_codon_sequence, tmp_info):
    print(codon_list)
    print(tmp_info)
    print("Original sequence:", orig_codon_sequence)
    print("Original aa:", CodonDict[orig_codon_sequence][1])
    tmp_codon_sequence = ""
    for x in range(3):
        if tmp_info[0][1] == x:
            tmp_codon_sequence += tmp_info[0][0]
        else:
            tmp_codon_sequence += orig_codon_sequence[x]
    print("Changed sequence:", tmp_codon_sequence)
    print("Changed aa:", CodonDict[tmp_codon_sequence][1])
    if CodonDict[orig_codon_sequence][1] == CodonDict[tmp_codon_sequence][1]:
        print("Type of change:", 'S')
    else:
        print("Type of change:", 'N')
    print('\n')
    
    '''
        if (line[8] > line[4]) and (line[4] > 12):
            codon_sequence += 'A'
            num_changes = line[4]/23
        elif (line[8] > line[5]) and (line[5] > 12):
            codon_sequence += 'C'
            num_changes = line[5]/23
        elif (line[8] > line[6]) and (line[6] > 12):
            codon_sequence += 'G'
            num_changes = line[6]/23
        elif (line[8] > line[7]) and (line[7] > 12):
            codon_sequence += 'T'
            num_changes = line[7]/23
        else:
            codon_sequence += line[3]
        if codon_position == 3:
            line.append(CodonDict[codon_sequence][0])
            codon_sequence = ""
            codon_position = 1
            str1 = ' '.join(str(e) for e in line)
            #out_file.write(' '.join(line))
        else:
            codon_position += 1
'''

with open("Mapourika_Histones_4/MP2_R1.fastq.Histone_H2A.raw", "r") as raw_file:
    codon_list = []
    position = 0
    codon_sequence = ""
    need_to_run_test = False
    tmp_sequence = []
    tmp_base = ""
    for line in raw_file:
        line = line.split()
        if line[0][0] != "#":
            TEfam = line[1]
            sample_id = line[2]
            refbase = line[3]
            A = int(line[4])
            C = int(line[5])
            G = int(line[6])
            T = int(line[7])
            if refbase == 'A':
                if (C > 12):
                    tmp_base += 'C'
                if (G > 12):
                    tmp_base += 'G'
                if (T > 12):
                    tmp_base += 'T'
                if tmp_base != "":
                    need_to_run_test = True
                    info = tmp_base, position
                    tmp_sequence.append(info)
                    tmp_base = ""
            elif refbase == 'C':
                if (A > 12):
                    tmp_base += 'A'
                if (G > 12):
                    tmp_base += 'G'
                if (T > 12):
                    tmp_base += 'T'
                if tmp_base != "":
                    need_to_run_test = True
                    info = tmp_base, position
                    tmp_sequence.append(info)
                    tmp_base = ""
            elif refbase == 'G':
                if (A > 12):
                    tmp_base += 'A'
                if (C > 12):
                    tmp_base += 'C'
                if (T > 12):
                    tmp_base += 'T'
                if tmp_base != "":
                    need_to_run_test = True
                    info = tmp_base, position
                    tmp_sequence.append(info)
                    tmp_base = ""
            elif refbase == 'T':
                if (A > 12):
                    tmp_base += 'A'
                if (C > 12):
                    tmp_base += 'C'
                if (G > 12):
                    tmp_base += 'G'
                if tmp_base != "":
                    need_to_run_test = True
                    info = tmp_base, position
                    tmp_sequence.append(info)
                    tmp_base = ""
            codon_list.append(line)
            codon_sequence += line[3]
            if (position == 2):
                if (need_to_run_test == True):
                    run_codon(codon_list, codon_sequence, tmp_sequence)
                codon_list = []
                position = 0
                codon_sequence = ""
                need_to_run_test = False
                tmp_sequence = []
                tmp_base = ""
            else:
                position += 1

