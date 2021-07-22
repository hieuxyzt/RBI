import math
class Equation2_22:
    def phi(x):
        #'Cumulative distribution function for the standard normal distribution'
        return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
    def Equation2_22(PoP1,B1,PoP2,B2,PoP3,B3):
        return (PoP1*Equation2_22.phi(-1.0 * B1)+
            PoP2*Equation2_22.phi(-1.0 * B2)+
            PoP3*Equation2_22.phi(-1.0 * B3)
            )/(1.56E-04)