from inputs import Layup
from analysis import Analysis

def run_analysis(material, dia_is, ttl_lyrss, omegas, h):
    """ (Material, list, list, list) -> Dictionary
    Return dictionary of analysis results based on range of input data.
    """

    analyses = {}
    
    for dia_i in dia_is:
        
        analyses[dia_i] = {}
        
        for omega in omegas:
            
            analyses[dia_i][omega] = {}
            
            for ttl_lyrs in ttl_lyrss:

                layup = Layup(dia_i, omega, ttl_lyrs, h)
                analysis = Analysis(layup, material)
                analyses[dia_i][omega][ttl_lyrs] = analysis
                
    return analyses