from wf_dataprocessing import processing_data
from wf_visualization import computing_summary_stats, computing_correlations, generating_plots

def main():
    processing_data()
    computing_summary_stats()
    computing_correlations()
    generating_plots()
    
if __name__ == "__main__":
    main()