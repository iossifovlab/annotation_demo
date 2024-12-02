#!/usr/bin/env python

from dae.genomic_resources.reference_genome import build_reference_genome_from_resource_id
from dae.genomic_resources.genomic_scores import build_score_from_resource_id
from dae.genomic_resources.gene_models import build_gene_models_from_resource_id



###################
#### TO REMOVE ####
###################
from dae.genomic_resources.genomic_scores import PositionScore

def get_region_score(ps: PositionScore, chrom: str, beg: int, end: int, score_id: str):
    r = [None] * (end - beg + 1)
    for b, e, (v) in ps.fetch_region(chrom, beg, end, [score_id]):
        if e > end:
            e = end
        r[b-beg:e-beg+1] = v
    return r
###################
###################
###################

chrom, pos_beg, pos_end = ("chr16", 30108313, 30108420)

# ref = build_reference_genome_from_resource_id("hg38/genomes/GRCh38.p14").open()
# print("The sequence is:", ref.get_sequence(chrom, pos_beg, pos_end))

# gm = build_gene_models_from_resource_id("hg38/gene_models/GENCODE/46/comprehensive/ALL").load()
# for tm in gm.gene_models_by_location(chrom, pos_beg, pos_end):
#     print(tm.tr_id, tm.gene, tm.is_coding(), tm.cds_len())

# ps = build_score_from_resource_id("hg38/scores/phyloP100way").open()
# print(get_region_score(ps, chrom, pos_beg, pos_end, "phyloP100way"))

# ass = build_score_from_resource_id("hg38/variant_frequencies/gnomAD_4.1.0/exomes/ALL").open()
