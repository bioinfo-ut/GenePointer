from gene_pointer import analyse_genomes
from subprocess import call
import os
import time
from Bio import SeqIO
from Bio.Seq import Seq

basedir = "/home/sass/Dev/PhenotypeSeeker"
bacteria_and_ref_genome_and_gff = {
    "mycobacterium tuberculosis": [basedir + "/GeneFinder1/RefGenomes/MycoTuber/GCA_000195955.2_ASM19595v2_genomic.fna", basedir + "/GeneFinder1/RefGenomes/MycoTuber/genomic.gff"],
    "klebsiella pneumoniae": [basedir + "/GeneFinder1/RefGenomes/KlebsPneum/GCF_023546055.1_ASM2354605v1_genomic.fna", basedir + "/GeneFinder1/RefGenomes/KlebsPneum/genomic.gff"],
    "escherichia coli": [basedir + "/GeneFinder1/RefGenomes/EColi/GCA_000005845.2_ASM584v2_genomic.fna", basedir + "/GeneFinder1/RefGenomes/EColi/genomic.gff"],
    "pseudomonas aeruginosa": [basedir + "/GeneFinder1/RefGenomes/PseudoAerugi/GCA_000006765.1_ASM676v1_genomic.fna", basedir + "/GeneFinder1/RefGenomes/PseudoAerugi/genomic.gff"],
    "enterococcus faecium": [basedir + "/GeneFinder1/RefGenomes/EnteroFaecium/GCF_003071425.1_ASM307142v1_genomic.fna", basedir + "/GeneFinder1/RefGenomes/EnteroFaecium/genomic.gff"],
    "staphylococcus aureus": [basedir + "/GeneFinder1/RefGenomes/StaphylAureus/GCA_000013425.1_ASM1342v1_genomic.fna", basedir + "/GeneFinder1/RefGenomes/StaphylAureus/genomic.gff"],
    "streptococcus pneumoniae": [basedir + "/GeneFinder1/RefGenomes/StreptoPneum/GCA_001457635.1_NCTC7465_genomic.fna", basedir + "/GeneFinder1/RefGenomes/StreptoPneum/genomic.gff"],
    "salmonella enterica": [basedir + "/GeneFinder1/RefGenomes/SalmEnter/GCA_000006945.2_ASM694v2_genomic.fna", basedir + "/GeneFinder1/RefGenomes/SalmEnter/genomic.gff"],
}

def main():

    SPECIES = "enterococcus faecium"
    ANTIBIOTIC = "vancomycin"
    REFSEQ = bacteria_and_ref_genome_and_gff[SPECIES][0]
    GFF = bacteria_and_ref_genome_and_gff[SPECIES][1]

    start = time.time()
    
    analyse_genomes.find_genes_alignment("significant_lines_from_kmer_coeff_file.txt", SPECIES , ANTIBIOTIC, GFF, ref_genome_file = REFSEQ, reduce_kmers_to=10)
    
    print("Time taken for find_gene2.py: ", round((time.time()-start), 6), " s")


if __name__ == "__main__":
    main()