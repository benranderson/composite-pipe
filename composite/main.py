#==============================================================================
# Title:            CompStiff
# Version:          1
# Author:           Ben Randerson
# Date:             14/01/15
# Python Version:   3.4
# Description:      Calculate axial, bending and torsional stiffnesses for
#                   prescribed composite pipe properties.
#
#                   Results output as tables in .txt files and graphs in
#                   .png files.
#
#                   Mechanical behaviour of composite pipe based on methodology
#                   in "Composite Materials in Piping Applications", Dimitrios
#                   G. Pavlou.
#==============================================================================

from extract_inputs import extract_inputs
from run_analysis import run_analysis
from post_pro import post_pro

def main():
    """ Run program.
    """

    # Extract input variables from data.py
    material, dia_is, ttl_lyrss, omegas, h = extract_inputs()

    # Run analyses
    analyses = run_analysis(material, dia_is, ttl_lyrss, omegas, h)

    # Post process results
    post_pro(dia_is, ttl_lyrss, omegas, analyses)

if __name__ == "__main__":
    main()
