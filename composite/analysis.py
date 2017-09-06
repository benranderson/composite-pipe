from mech_behav import MechBehav
from stiffness import Stiffness

class Analysis:
    
    def __init__(self, layup, material):
        
        self.layup = layup
        self.material = material
        self.calculation = Calculation(self.layup, self.material)
        self.result = Result(self.calculation.stiffness.EA, self.calculation.stiffness.JG, self.calculation.stiffness.EI)
        
        
class Calculation:
    
    def __init__(self, layup, material):
        
        self.mech_behav = MechBehav(layup, material)
        self.stiffness = Stiffness(self.mech_behav.abd, layup)
        
        
class Result:
    
    def __init__(self, EA, JG, EI):
        
        self.EA = EA
        self.JG = JG
        self.EI = EI
    
    
