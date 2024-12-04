#!/usr/bin/env python

from dae.genomic_resources.reference_genome import build_reference_genome_from_resource_id
from dae.genomic_resources.genomic_scores import build_score_from_resource_id
from dae.genomic_resources.gene_models import build_gene_models_from_resource_id

chrom, pos_beg, pos_end = ("chr16", 30108313, 30108333)

print("SEQUENCE")
ref = build_reference_genome_from_resource_id("hg38/genomes/GRCh38.p14").open()
print(ref.get_sequence(chrom, pos_beg, pos_end))

print("\nTRANSCRIPTS")
gm = build_gene_models_from_resource_id("hg38/gene_models/MANE/1.3").load()
for tm in gm.gene_models_by_location(chrom, pos_beg, pos_end):
    print(tm.tr_id, tm.gene, tm.is_coding(), tm.cds_len())

print("\nSCORE")
ps = build_score_from_resource_id("hg38/scores/phyloP100way").open()
print(ps.get_region_scores(chrom, pos_beg, pos_end, "phyloP100way"))

print("\nVARIANTS")
ass = build_score_from_resource_id("hg38/variant_frequencies/gnomAD_4.1.0/exomes/ALL").open()
for pos, ref, alt, [score] in ass.fetch_region(chrom, pos_beg, pos_end, ["AF"]):
    print(pos, ref, alt, score)
