from SigProfilerExtractor import sigpro as sig

if __name__ == '__main__':
    sig.sigProfilerExtractor(
        input_type = "matrix",
        output = "Results/LUAD_Signatures",
        input_data = "Raw_Data/LUAD_input/output/SBS/LUAD.SBS96.all",
        reference_genome = "GRCh38",
        minimum_signatures = 1,
        maximum_signatures = 10,
        nmf_replicates = 10,
        cpu = 2
    )