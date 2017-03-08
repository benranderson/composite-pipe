from data import * # Import input data (note h is imported)
import math
import numpy as np
from inputs import Material

def extract_inputs():
    """ () -> Material, list, list, list
    Define material object and populate input lists with data extracted from 
    data.py file.
    """

    material = Material(E_1, E_2, E_3, v_12, v_13, v_23, G_12, G_13, G_23)
    dia_is = list(np.arange(dia_i_min,dia_i_max+0.5*dia_i_step,dia_i_step))
    ttl_lyrss = list(range(ttl_lyrss_min,ttl_lyrss_max+ttl_lyrss_step,ttl_lyrss_step))
    omega_min_rad = omega_min * (math.pi/180)
    omega_max_rad = omega_max * (math.pi/180)
    omega_step_rad = omega_step * (math.pi/180)
    omegas = list(np.arange(omega_min,omega_max_rad+0.5*omega_step_rad,omega_step_rad))

    return material, dia_is, ttl_lyrss, omegas, h