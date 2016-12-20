import math
import numpy as np

class Strain:
    
    def __init__(self, load, abd, layup):
        
        N = load.N
        P = load.P
        T = load.T

        h = layup.h
        dia_m = layup.dia_m
        
        eps0_a = self.axial(N, abd, dia_m)
        eps0_p = self.pressure(P, abd, dia_m)
        eps0_t = self.torsion(T, abd, dia_m)
        
        eps0 = np.matrix(np.zeros((6,1)))
        
        for i in range(0, 6):
            eps0[i,0] = eps0_a[i,0] + eps0_p[i,0] + eps0_t[i,0]
            
        self.eps = np.matrix(np.zeros((3,1)))
        
        for i in range(0, 3):
            self.eps[i,0] = eps0[i,0] + 0.5*h*eps0[i+3,0]

            
            
    def axial(self, N, abd, dia_m):
        """ (Strain, number, Matrix, number) -> Matrix
        Return matrix of strains due to axial tension load.
        """
            
        Nx = N/(math.pi*dia_m)
        
        eps0 = np.matrix(np.zeros((6,1)))
        
        for i in range(0, 6):
            eps0[i,0] = abd[i,0]*Nx
            
        return eps0
    
            
    def pressure(self, P, abd, dia_m):
        """ (Strain, number, Matrix, number) -> Matrix
        Return matrix of strains due to pressure load.
        """
            
        Ny = 0.5*P*dia_m
        
        eps0 = np.matrix(np.zeros((6,1)))
        
        for i in range(0, 6):
            eps0[i,0] = abd[i,1]*Ny
            
        return eps0
            
            
    def torsion(self, T, abd, dia_m):
        """ (Strain, number, Matrix, number) -> Matrix
        Return matrix of strains due to torque load.
        """
            
        Tx = 2*T/(math.pi*dia_m**2)
        
        eps0 = np.matrix(np.zeros((6,1)))
        
        for i in range(0, 6):
            eps0[i,0] = abd[i,2]*Tx
            
        return eps0