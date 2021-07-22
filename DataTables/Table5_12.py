from .. import DataGlobal
from ..Enum import Effectiveness
class Table5_12 :
    data = None
    def FindDamageFactor(self,Art, inspections, effectiveness):
        if self.data == None:
            
            self.Init()
            
        index = 0
        if inspections > 0.0:
            
            index = self.GetIndex(effectiveness)
            
        Art = max([0.05, min([1.0, Art])])
        inspections = max[1.0, min([inspections, 1.0])]
        for i in  range(self.data.Count):
            if (self.data[i].inspections == inspections) & (self.data[i].art >= Art):
                return self.data[i].Df[index]
            
        return 0.0
        

    def FindNearestHigherArtValue(self,Art):
        
        if self.data == None:
        
            self.Init()
        
        Art = max([0.05, min([1.0, Art])])
        for i in range(self.data.Count):
        
            if self.data[i].art >= Art:
                return self.data[i].art
            
        
        return 0.0
        
    def GetIndex(eff):
        switcher={
                Effectiveness.Ineffective:0,
                Effectiveness.UsuallyEffective:3,
                Effectiveness.FairlyEffective:2,
                Effectiveness.PoorlyEffective:1,
                Effectiveness.HighlyEffective:4,
                }
        return switcher.get(eff,0)
           
    def Init(self):
      
        self.data = DataGlobal.table5_12Data
      
   
