annotate_columns simple_input.txt simple_pipeline.yaml -f -j 1 -o results/simple_input_simple_pipeline.txt &

annotate_vcf simple_input.vcf simple_pipeline.yaml -f -j 1 -o results/simple_input_simple_pipeline.vcf &

annotate_columns regions_input.txt simple_pipeline.yaml -f -j 1 -o results/regions_input_simple_pipeline.txt &
annotate_columns regions_input.txt regions_pipeline.yaml -f -j 1 -o results/regions_input_regions_pipeline.txt &

annotate_columns simple_input.txt complex_pipeline.yaml -f -j 1 -o results/simple_input_complex_pipeline.txt &
annotate_vcf simple_input.vcf complex_pipeline.yaml -f -j 1 -o results/simple_input_complex_pipeline.vcf &

annotate_columns simple_input.txt pipeline/Autism_annotation -j 1 -o results/simple_input_autism_pipeline.txt &
annotate_vcf simple_input.vcf pipeline/Autism_annotation -f -j 1 -o results/simple_input_autism_pipeline.vcf &

