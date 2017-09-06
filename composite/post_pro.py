import math
import numpy as np
from prettytable import PrettyTable

import matplotlib
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use('Agg') # Enable plotting in c9
import matplotlib.pyplot as plt

# Set plot text format
font = {'weight' : 'regular',
        'size'   : 8}
matplotlib.rc('font', **font)

def post_pro(dia_is, ttl_lyrss, omegas, analyses):
    
    # Populate list for table header 
    omega_title = 'Fibre Or. [deg]'
    table_header = [omega_title]
    for ttl_lyrs in ttl_lyrss:
        table_header.append(str(ttl_lyrs) + ' Layers')
        
    # Convert fibre orientations from radians to degrees for reporting
    omegas_deg = [x * (180/math.pi) for x in omegas] 
        
    # Define grid of total layers and fibre orientations for x, y values in graphs
    X, Y = np.meshgrid(ttl_lyrss, omegas_deg)
    
    # Row and column sizes for resizing stiffness mesh (z values) for graphs
    xx = len(omegas)
    yy = len(ttl_lyrss)
    
    with open('output/tab_axial.csv', 'w') as out_axial, open('output/tab_bend.csv', 'w') as out_bend, open('output/tab_tors.csv', 'w') as out_tors:
        
        # Output files headers
        out_axial.write('Axial Stiffness [N]')
        out_bend.write('Bending Stiffness [Nm^2]')
        out_tors.write('Torsional Stiffness [Nm^2]')
    
        for dia_i in dia_is:

            out_axial.write('\n\nDia: ' + str(dia_i) + ' m\n')
            out_bend.write('\n\nDia: ' + str(dia_i) + ' m\n')
            out_tors.write('\n\nDia: ' + str(dia_i) + ' m\n')
            
            # Stiffness (z) values for graphs for each diameter
            stiff_axial = []
            stiff_bend = []
            stiff_tors = []
            
            # Initiate results table objects
            table_axial = PrettyTable(table_header)
            table_bend = PrettyTable(table_header)
            table_tors = PrettyTable(table_header)
            
            table_axial.float_format = ".2"
            table_bend.float_format = ".2"
            table_tors.float_format = ".2"

            table_axial.float_format[omega_title] = ".1"
            table_bend.float_format[omega_title] = ".1"
            table_tors.float_format[omega_title] = ".1"
            
            # One space between column edges and contents (default)
            table_axial.padding_width = 1 
            table_bend.padding_width = 1
            table_tors.padding_width = 1
            
            for omega in omegas:
                
                # Convert angle to degrees for reporting
                omega_deg = omega * (180/math.pi) 
                
                table_row_axial = [omega_deg]
                table_row_bend = [omega_deg]
                table_row_tors = [omega_deg]

                for ttl_lyrs in ttl_lyrss:

                    stiff_axial.append(analyses[dia_i][omega][ttl_lyrs].result.EA)
                    stiff_bend.append(analyses[dia_i][omega][ttl_lyrs].result.EI)
                    stiff_tors.append(analyses[dia_i][omega][ttl_lyrs].result.JG)
                    
                    table_row_axial.append(analyses[dia_i][omega][ttl_lyrs].result.EA)
                    table_row_bend.append(analyses[dia_i][omega][ttl_lyrs].result.EI)
                    table_row_tors.append(analyses[dia_i][omega][ttl_lyrs].result.JG)
                    
                table_axial.add_row(table_row_axial)
                table_bend.add_row(table_row_bend)
                table_tors.add_row(table_row_tors)
                
            # Print tables to results output files
            out_axial.write(str(table_axial))
            out_bend.write(str(table_bend))
            out_tors.write(str(table_tors))
            

            # Generate graphs
            fig1 = plt.figure()
            fig1.suptitle('Axial Stiffness - ' + str(dia_i) + 'm Dia', fontsize=10, fontweight='bold')
            ax1 = fig1.add_subplot(111, projection='3d')
            ax1.plot_surface(X, Y, np.reshape(stiff_axial,(xx,yy)), cmap=plt.cm.jet, cstride=1, rstride=1)
            ax1.set_xlabel('Number of Layers')
            ax1.set_ylabel('Fibre Orientation [deg]')
            ax1.set_zlabel('Axial Stiffness [N]')
            fig1.savefig('output/graph_axial_' + str(dia_i) + 'm.png')
            
            fig2 = plt.figure()
            fig2.suptitle('Torsional Stiffness - ' + str(dia_i) + 'm Dia', fontsize=10, fontweight='bold')
            ax2 = fig2.add_subplot(111, projection='3d')
            ax2.plot_surface(X, Y, np.reshape(stiff_tors,(xx,yy)), cmap=plt.cm.jet, cstride=1, rstride=1)
            ax2.set_xlabel('Number of Layers')
            ax2.set_ylabel('Fibre Orientation [deg]')
            ax2.set_zlabel('Torsional Stiffness [Nm^2]')
            fig2.savefig('output/graph_tors_' + str(dia_i) + 'm.png')
            
            fig3 = plt.figure()
            fig3.suptitle('Bending Stiffness - ' + str(dia_i) + 'm Dia', fontsize=10, fontweight='bold')
            ax3 = fig3.add_subplot(111, projection='3d')
            ax3.plot_surface(X, Y, np.reshape(stiff_bend,(xx,yy)), cmap=plt.cm.jet, cstride=1, rstride=1)
            ax3.set_xlabel('Number of Layers')
            ax3.set_ylabel('Fibre Orientation [deg]')
            ax3.set_zlabel('Bending Stiffness [Nm^2]')
            fig3.savefig('output/graph_bend_' + str(dia_i) + 'm.png')
            

                    