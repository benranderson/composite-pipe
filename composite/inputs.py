class Composite:
    
    def __init__(self, layup, material):
        """ (Composite) -> NoneType
        """
        
        self.layup = layup
        self.material = material
        
        
class Layup:
    
    def __init__(self, dia_i, omega, ttl_lyrs, h):
        """ (Layup, number, number, int, number) -> NoneType
        Create a composite layup with:
            - inner diameter: dia_i
            - fibre orientation: omega
            - number of layers: ttl_lyrs
            - layer thickness: h
        """
        
        self.omega = omega
        self.dia_i = dia_i
        self.ttl_lyrs = ttl_lyrs
        self.h = h
        
        self.dia_o = dia_i + 2*ttl_lyrs*h
        self.dia_m = 0.5*(self.dia_i+self.dia_o)
        
class Material:
        
    def __init__(self, E_1, E_2, E_3, v_12, v_13, v_23, G_12, G_13, G_23):
        """ (Material, number, number, number, number, number, number, 
        number, number, number) -> NoneType
        """
        
        self.E_1 = E_1
        self.E_2 = E_2
        self.E_3 = E_3
        
        self.v_12 = v_12
        self.v_13 = v_13
        self.v_23 = v_23
        
        self.G_12 = G_12
        self.G_13 = G_13
        self.G_23 = G_23
        
        self.v_32 = self.v_23*E_3/E_2
        self.v_21 = self.v_12*E_2/E_1
        
class Load:
    
    def __init__(self, N, P, T, M):
        """ (Load, number, number, number, number) -> NoneType
        """
        
        self.N = N
        self.P = P
        self.T = T
        self.M = M