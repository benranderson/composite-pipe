import math
import scipy.integrate
from inputs import Load
from strain import Strain


class Stiffness:
    
    def __init__(self, abd, layup):
        
        dia_o = layup.dia_o
        dia_i = layup.dia_i
        omega = layup.omega
        
        r_o = 0.5*layup.dia_o
        
        # AXIAL STIFFNESS
        
        load_a = Load(1,0,0,0)
        strain_a = Strain(load_a, abd, layup)
        self.EA = 1/strain_a.eps[0,0]
        
        # TORSIONAL STIFFNESS
        
        load_t = Load(0,0,1,0)
        strain_t = Strain(load_t, abd, layup)
        self.JG = r_o/strain_t.eps[2,0]
        
        # BENDING STIFFNESS

        z = 0.5*layup.dia_i*math.cos(omega)
        
        def stiffness(omega):
            return (1/abd[0,0])*z**2 + (1/abd[3,3])*math.cos(omega)**2
        
        # Determine intergral using scipy's integrate.quad function.
        # The function return value is a tuple, with the first element holding 
        # the estimated value of the integral and the second element holding an
        # upper bound on the error. [0] index used to return estimated value.
        self.EI = dia_i*scipy.integrate.quad(lambda omega: stiffness(omega), 0, math.pi)[0]