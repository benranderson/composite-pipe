#==============================================================================
#
# COMPSTIFF INPUT DATA
#
#==============================================================================

# MATERIAL DATA ===============================================================

# Young's Moduli
E_1 = 3.24e10
E_2 = 8.24e8
E_3 = 8.24e8

# Poisson's Ratios
v_12 = 0.008
v_13 = 0.008
v_23 = 0.62

# Shear Moduli
G_12 = 2.77e8
G_13 = 2.77e8
G_23 = 2.54e8

# LAYUP DATA ==================================================================

# Layer Thickness
h = (10e-3)/44

# Inner Diameter Range
dia_i_min = 0.06
dia_i_max = 0.06
dia_i_step = 0.1

# Number of Layers Range
ttl_lyrss_min = 40
ttl_lyrss_max = 40
ttl_lyrss_step = 2

# Fibre Orientation Range
omega_min = 0
omega_max = 90
omega_step = 5