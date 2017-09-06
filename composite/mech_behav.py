import math
import numpy as np

class MechBehav:
    
    def __init__(self, layup, material):
        
        omega = layup.omega
        ttl_lyrs = layup.ttl_lyrs
        h = layup.h
        
        E_1 = material.E_1
        E_2 = material.E_2
        E_3 = material.E_3
        
        v_12 = material.v_12
        v_13 = material.v_13
        v_21 = material.v_21
        v_23 = material.v_23
        v_32 = material.v_32
        
        G_12 = material.G_12
        G_13 = material.G_13
        G_23 = material.G_23
    
        S = np.matrix(np.zeros((6,6)))
        
        S[0,0] = 1 / E_1
        S[0,1] = -v_12 / E_2
        S[0,2] = -v_13 / E_3
        S[1,0] = -v_12 / E_1
        S[1,1] = 1 / E_2
        S[1,2] = -v_23 / E_3
        S[2,0] = -v_13 / E_1
        S[2,1] = -v_23 / E_2
        S[2,2] = 1 / E_3
        S[3,3] = 1 / G_23
        S[4,4] = 1 / G_13
        S[5,5] = 1 / G_12
        
        Q = np.matrix(np.zeros((6,6)))
        
        Q[0,0] = S[1,1] / (S[0,0]*S[1,1] - S[0,1]*S[0,1])
        Q[0,1] = -S[0,1] / (S[0,0]*S[1,1] - S[0,1]*S[0,1])
        Q[1,0] = -S[0,1] / (S[0,0]*S[1,1] - S[0,1]*S[0,1])
        Q[1,1] = S[0,0] / (S[0,0]*S[1,1] - S[0,1]*S[0,1])
        Q[5,5] = 1 / S[5,5]
        
        def pop_QQ(omega, i, j):
        
            eqns = {0: {0: Q[0,0]*(math.cos(omega))**4 + 2*(Q[0,1]+2*Q[5,5])*(math.sin(omega))**2*(math.cos(omega))**2 + Q[1,1]*(math.sin(omega))**4,
            1: (Q[0,0]+Q[1,1]-4*Q[5,5])*(math.sin(omega))**2*(math.cos(omega))**2 + Q[0,1]*((math.sin(omega))**4+(math.cos(omega))**4),
            5: (Q[0,0]-Q[0,1]-2*Q[5,5])*math.sin(omega)*(math.cos(omega))**3 + (Q[0,1]-Q[1,1]+2*Q[5,5])*(math.sin(omega))**3*math.cos(omega)},
            1: {1: Q[0,0]*(math.sin(omega))**4 + 2*(Q[0,1]+2*Q[5,5])*(math.sin(omega))**2*(math.cos(omega))**2 + Q[1,1]*(math.cos(omega))**4,
            5: (Q[0,0]-Q[0,1]-2*Q[5,5])*(math.sin(omega))**3*math.cos(omega) + (Q[0,1]-Q[1,1]+2*Q[5,5])*math.sin(omega)*(math.cos(omega))**3},
            5: {5: (Q[0,0]+Q[1,1]-2*Q[0,1]-2*Q[5,5])*(math.sin(omega))**2*(math.cos(omega))**2 + Q[5,5]*((math.sin(omega))**4+(math.cos(omega))**4)}}
            
            QQ = eqns[i][j]
            
            return QQ
    
        self.A = np.matrix(np.zeros((6,6)))
        self.B = np.matrix(np.zeros((6,6)))
        self.D = np.matrix(np.zeros((6,6)))
        
        ijs = [{"i": 0, "j": 0}, {"i": 0, "j": 1}, {"i": 0, "j": 5}, 
            {"i": 1, "j": 1}, {"i": 1, "j": 5}, {"i": 5, "j": 5}]
    
        for ij in ijs:
            for k in range(1, ttl_lyrs+1):
                self.A[ij["i"],ij["j"]] += pop_QQ((-1)**k*omega, ij["i"], ij["j"]) * (k*h - (k-1)*h)
                self.B[ij["i"],ij["j"]] += pop_QQ((-1)**k*omega, ij["i"], ij["j"]) * ((k*h)**2 - ((k-1)*h)**2)
                self.D[ij["i"],ij["j"]] += pop_QQ((-1)**k*omega, ij["i"], ij["j"]) * ((k*h)**3 - ((k-1)*h)**3)
                
            self.B[ij["i"],ij["j"]] *= 0.5
            self.D[ij["i"],ij["j"]] *= 1/3
        
        # LAMINATE STIFFNESS MATRIX
        
        self.ABD = np.matrix(np.zeros((6,6)))
        
        self.ABD[0,0] = self.A[0,0]
        self.ABD[0,1] = self.A[0,1]
        self.ABD[0,2] = self.A[0,5]
        self.ABD[0,3] = self.B[0,0]
        self.ABD[0,4] = self.B[0,1]
        self.ABD[0,5] = self.B[0,5]
        
        self.ABD[1,0] = self.A[0,1]
        self.ABD[1,1] = self.A[1,1]
        self.ABD[1,2] = self.A[1,5]
        self.ABD[1,3] = self.B[0,1]
        self.ABD[1,4] = self.B[1,1]
        self.ABD[1,5] = self.B[1,5]
        
        self.ABD[2,0] = self.A[0,5]
        self.ABD[2,1] = self.A[1,5]
        self.ABD[2,2] = self.A[5,5]
        self.ABD[2,3] = self.B[0,5]
        self.ABD[2,4] = self.B[1,5]
        self.ABD[2,5] = self.B[5,5]
        
        self.ABD[3,0] = self.B[0,0]
        self.ABD[3,1] = self.B[0,1]
        self.ABD[3,2] = self.B[0,5]
        self.ABD[3,3] = self.D[0,0]
        self.ABD[3,4] = self.D[0,1]
        self.ABD[3,5] = self.D[0,5]
        
        self.ABD[4,0] = self.B[0,1]
        self.ABD[4,1] = self.B[1,1]
        self.ABD[4,2] = self.B[1,5]
        self.ABD[4,3] = self.D[0,1]
        self.ABD[4,4] = self.D[1,1]
        self.ABD[4,5] = self.D[1,5]
        
        self.ABD[5,0] = self.B[0,5]
        self.ABD[5,1] = self.B[1,5]
        self.ABD[5,2] = self.B[5,5]
        self.ABD[5,3] = self.D[0,5]
        self.ABD[5,4] = self.D[1,5]
        self.ABD[5,5] = self.D[5,5]
        
        self.abd = self.ABD.I
        
        # REDUCED STIFFNESES
        
        self.QQ = np.matrix(np.zeros((3,3)))
        
        self.QQ[0,0] = pop_QQ(omega, 0, 0)
        self.QQ[0,1] = pop_QQ(omega, 0, 1)
        self.QQ[0,2] = pop_QQ(omega, 0, 5)
        self.QQ[1,0] = pop_QQ(omega, 0, 1)
        self.QQ[1,1] = pop_QQ(omega, 1, 1)
        self.QQ[1,2] = pop_QQ(omega, 1, 5)
        self.QQ[2,0] = pop_QQ(omega, 0, 5)
        self.QQ[2,1] = pop_QQ(omega, 1, 5)
        self.QQ[2,2] = pop_QQ(omega, 5, 5)
        
        # TRANSFORMATION MATRIX
        
        self.T = np.matrix(np.zeros((3,3)))
        
        self.T[0,0] = math.cos(omega)**2
        self.T[0,1] = math.sin(omega)**2
        self.T[0,2] = 2*math.cos(omega)*math.sin(omega)
        self.T[1,0] = math.sin(omega)**2
        self.T[1,1] = math.cos(omega)**2
        self.T[1,2] = -2*math.cos(omega)*math.sin(omega)
        self.T[2,0] = -math.cos(omega)*math.sin(omega)
        self.T[2,1] = math.cos(omega)*math.sin(omega)
        self.T[2,2] = math.cos(omega)**2 - math.sin(omega)**2