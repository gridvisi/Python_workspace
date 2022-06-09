# https://www.codewars.com/kata/dna-to-rna-conversion/python

dna = 'GCAT'
def DNAtoRNA(dna):
    dna_ls = list(dna)
    for i,e in enumerate(dna_ls):
        if dna_ls[i] =='T':
            dna_ls[i] ='U'
    return ''.join(dna_ls)
print(DNAtoRNA(dna))

def DNAtoRNA(dna):
    return dna.replace('T', 'U')