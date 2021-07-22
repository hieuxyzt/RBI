from Enum.TankSettelmentCondition import TankSettlementCondition
from Enum.ComponentType import ComponentType
from ..DataTables import Table4_5
from ..DataTables import Table4_6
from ..DataTables import Table5_12
from ..DataTables import Table5_13
import ThinningDFData
from ..Caculators import CalcHelpers
from ..Caculators import CalcEquation2_22
import math
import ThinningDFData
class ThinningDFCalculator:
    def hasValue(variable):
        return variable!=None and not variable and isinstance(variable, (int, float))
    defaultDF = 6500.0   
    def Calculate(self,data):
            self._data = ThinningDFData(data)
            self._data.Age = []
            self._data.PosteriorProbabilities = []
            self._data.ConditionalProbabilityInspection = []
            self._data.DamageFactor = []
            self._data.BaseDamageFactorTank = []
            self._data.CorrosionRateFactorForDamageState = []
            self._data.PressureCoefficientOfVariance = 0.05
            self._data.FlowStressCoefficientOfVariance = 0.2
            self._data.ThinningCoefficientOfVariance = 0.2
            self._data.CorrosionRateFactorForDamageState[0] = 1.0
            self._data.CorrosionRateFactorForDamageState[1] = 2.0
            self._data.CorrosionRateFactorForDamageState[2] = 4.0
            self.table4_5 = Table4_5()
            self.table4_6 = Table4_6()
            self.table5_12 = Table5_12()
            self.table5_13 = Table5_13()
            #thickness without Cladding/t bm
            num = self._data.NominalThickness
            if(self._data.ComponentCladded):
                num = self._data.NominalThickness - self._data.CladdingThickness
            self._data.RAP = CalcHelpers.AP(self._data.AssessmentPeriod)
            #is the in-service time that the damage is applied
            #list3 of years
            self._data.Age = CalcHelpers.YearsFromCommisionDate(self._data.AssessmentDate, self._data.StartOrCommissioningDate, self._data.AssessmentPeriod)
            if (self._data.LastInspectionThickness > 0.0):
                #list3 of years
                self._data.AgeTk = CalcHelpers.InServiceTime(self._data.AssessmentDate, self._data.LatestInspectionDate, self._data.RAP)
            
            else:
                self._data.AgeTk = self._data.Age
        
            #tRdi  
            if self._data.LastInspectionThickness == 0.0:
                self._data.LastInspectionThickness = self._data.NominalThickness

            if (self._data.ComponentCladded):
                self._data.AgeRc = []
                for k in range(3):
                    #Equation2_11         
                    self._data.AgeRc[k] = max((float)(((self._data.LastInspectionThickness - num) / self._data.CladdingCorrosionRate) - ((float (self._data.RAP[k])) / 12.0)), (float)(0.0))
            self._data.BaseMetalThickness = num
            #Noneable = self._data.MinimumStructuralThicknessGovern ? self._data.StructuralThickness : self._data.MinRequireThickness
            #tMin
            Noneable = self._data.MinRequireThickness
            if self._data.MinimumStructuralThicknessGovern:
                #tC
                Noneable = self._data.StructuralThickness
            #Crbm
            if ThinningDFCalculator.hasValue(self._data.CurrentCorrosionRate):
  
                if (self._data.TankIsBottom):
              
                    if ThinningDFCalculator.hasValue(Noneable):
                 
                        self._data.Art = []
                        for m in range(3):
                            #is the component wall loss fraction since last inspection thickness measurement or service start date
                            #Atmospheric Storage Tank 
                            #Equation2.12
                            self._data.Art.append(self.table5_12.FindNearestHigherArtValue(max((float) (1.0 - ((self._data.LastInspectionThickness - (self._data.CurrentCorrosionRate * self._data.AgeTk[m])) / (Noneable + self._data.CorrosionAllowance))), (float) (0.0))))
                #Crcm
                elif not(self._data.ComponentCladded) :
                
                    self._data.WallLossWithoutCladding = []
                    for n in range(3):
                        #Equation2.13
                        self._data.WallLossWithoutCladding.append(max((float) ((self._data.CurrentCorrosionRate * self._data.AgeTk[n]) / self._data.LastInspectionThickness), (float)( 0.0)))
                    
                else:
                    #still is Art
                    self._data.WallLossWithCladding = []
                    self._data.AgeTkLessThanAgeRc = []
                    self._data.AgeTkMoreThanAgeRc = []
                    for num5 in range(3):
                        if (self._data.AgeTk[num5] < self._data.AgeRc[num5]):
                            #Equation2.14
                            self._data.WallLossWithCladding.append(max((float) ((self._data.CladdingCorrosionRate * self._data.AgeTk[num5]) / self._data.LastInspectionThickness), (float) (0.0)))
                            self._data.AgeTkLessThanAgeRc.append(True)
                            self._data.AgeTkMoreThanAgeRc.append(False)
                        
                        else:
                            #Equation2.15
                            self._data.WallLossWithCladding.append(((float) (((self._data.CladdingCorrosionRate * self._data.AgeRc[num5]) + (self._data.CurrentCorrosionRate * (self._data.AgeTk[num5] - self._data.AgeRc[num5]))) / self._data.LastInspectionThickness), (float) (0.0)))
                            self._data.AgeTkLessThanAgeRc.append(True)
                            self._data.AgeTkMoreThanAgeRc.append(False)
                
                #numArray = self._data.TankIsBottom ? self._data.Art : (self._data.ComponentCladded ? self._data.WallLossWithCladding : self._data.WallLossWithoutCladding)
                if self._data.TankIsBottom:
                    numArray = self._data.Art
                elif self._data.ComponentCladded:
                    numArray = self._data.WallLossWithCladding
                else:
                    numArray =  self._data.WallLossWithoutCladding
                if not(math.isnan(numArray[0])) and not(math.isinf(numArray[0])) and not(math.isnan(numArray[1])) and not(math.isinf(numArray[1])) and not(math.isnan(numArray[2])) and not(math.isinf(numArray[2])):
                    #Result Art 
                    self._data.WallLossFraction = [ numArray[0], numArray[1], numArray[2]]
            
            if (ThinningDFCalculator.hasValue(self._data.YieldStrength) and ThinningDFCalculator.hasValue(self._data.TensileStrength) and ThinningDFCalculator.hasValue(self._data.WeldJoint)) :
            
                designPressure = self._data.YieldStrength + self._data.TensileStrength
                #2.16
                self._data.FlowStress = (designPressure/2.0*self._data.WeldJoint)*1.1
                    
                if (self._data.MinimumStructuralThicknessGovern or self._data.EquipmentIsTank):
               
                    #S,tMin,tC
                    if ((ThinningDFCalculator.hasValue(self._data.AllowableStressTemperature) and ThinningDFCalculator.hasValue(self._data.MinRequireThickness)) and ThinningDFCalculator.hasValue(self._data.StructuralThickness)):
                        #2.17
                        weldJoint = (self._data.AllowableStressTemperature * self._data.WeldJoint) / self._data.FlowStress
                        structuralThickness = self._data.StructuralThickness
                        lastInspectionThickness = max(self._data.MinRequireThickness, structuralThickness) / self._data.LastInspectionThickness
                        self._data.StrengthRatio = (self._data.AllowableStressTemperature * self._data.WeldJoint) / self._data.FlowStress * max(self._data.MinRequireThickness, structuralThickness) / self._data.LastInspectionThickness
            
                #2.18
                elif (ThinningDFCalculator.hasValue(self._data.DesignPressure) and ThinningDFCalculator.hasValue(self._data.Diameter)):
                    self._data.StrengthRatioHoop = (self._data.DesignPressure*self._data.Diameter) / (self._data.shapeFactor * self._data.FlowStress * self._data.LastInspectionThickness) 
                    
            self._data.LevelConfidenceData = self.table4_5.Find(self._data.LevelConfidenceCorrosionRate)
            #check isNoneAndEmpty
            if (self._data.LevelConfidenceCorrosionRate == None or not self._data.LevelConfidenceCorrosionRate == str.e):
                self._data.LevelConfidenceData = [] #Confidence
            #2.19
            for i in range(3):  
                self._data.ConditionalProbabilityInspection[i] = (((self._data.LevelConfidenceData[i] * math.pow(self.table4_6.GetConditionalProbability(i)[0], self._data.NumberEffectivenessInspectionA)) * math.pow(self.table4_6.GetConditionalProbability(i)[1], self._data.NumberEffectivenessInspectionB)) * math.pow(self.table4_6.GetConditionalProbability(i)[2], self._data.NumberEffectivenessInspectionC)) * math.pow(self.table4_6.GetConditionalProbability(i)[3], self._data.NumberEffectivenessInspectionD)
            #2.20
            for j in range(3):
                self._data.PosteriorProbabilities[j] = self._data.ConditionalProbabilityInspection[j] / ((self._data.ConditionalProbabilityInspection[0] + self._data.ConditionalProbabilityInspection[1]) + self._data.ConditionalProbabilityInspection[2])
            
            if (ThinningDFCalculator.hasValue(self._data.FlowStress) and (self._data.WallLossFraction != None)):
                Noneable8 = self._data.StringthRatioHoop
                if(self._data.MinimumStructuralThicknessGovern or self._data.EquipmentIsTank):
                    Noneable8 = self._data.StrengthRatio
                if (ThinningDFCalculator.hasValue(Noneable8)):
                    self._data.Beta0AP = []
                    self._data.Beta1AP = []
                    self._data.Beta2AP = []
                    #2.21
                    for num10 in range(3):    
                        self._data.Beta0AP[num10] = ((1.0 - (self._data.CorrosionRateFactorForDamageState[num10] * self._data.WallLossFraction[0])) - Noneable8) / math.sqrt((((math.pow(self._data.CorrosionRateFactorForDamageState[num10], 2.0) * math.pow(self._data.WallLossFraction[0], 2.0)) * math.pow(self._data.ThinningCoefficientOfVariance, 2.0)) + (math.pow(1.0 - (self._data.CorrosionRateFactorForDamageState[num10] * self._data.WallLossFraction[0]), 2.0) * math.pow(self._data.FlowStressCoefficientOfVariance, 2.0))) + (math.pow(Noneable8, 2.0) * math.pow(self._data.PressureCoefficientOfVariance, 2.0)))
                        self._data.Beta1AP[num10] = ((1.0 - (self._data.CorrosionRateFactorForDamageState[num10] * self._data.WallLossFraction[1])) - Noneable8) / math.sqrt((((math.pow(self._data.CorrosionRateFactorForDamageState[num10], 2.0) * math.pow(self._data.WallLossFraction[1], 2.0)) * math.pow(self._data.ThinningCoefficientOfVariance, 2.0)) + (math.pow(1.0 - (self._data.CorrosionRateFactorForDamageState[num10] * self._data.WallLossFraction[1]), 2.0) * math.pow(self._data.FlowStressCoefficientOfVariance, 2.0))) + (math.pow(Noneable8, 2.0) * math.pow(self._data.PressureCoefficientOfVariance, 2.0)))
                        self._data.Beta2AP[num10] = ((1.0 - (self._data.CorrosionRateFactorForDamageState[num10] * self._data.WallLossFraction[2])) - Noneable8) / math.sqrt((((math.pow(self._data.CorrosionRateFactorForDamageState[num10], 2.0) * math.pow(self._data.WallLossFraction[2], 2.0)) * math.pow(self._data.ThinningCoefficientOfVariance, 2.0)) + (math.pow(1.0 - (self._data.CorrosionRateFactorForDamageState[num10] * self._data.WallLossFraction[2]), 2.0) * math.pow(self._data.FlowStressCoefficientOfVariance, 2.0))) + (math.pow(Noneable8, 2.0) * math.pow(self._data.PressureCoefficientOfVariance, 2.0)))
                    
            if (self._data.TankIsBottom):
                if (self._data.WallLossFraction == None):
                    for num11 in range(3):
                        self._data.BaseDamageFactorTank[num11] = self.defaultDF
                    
                else:
                    for num12 in range(3):
                        self._data.BaseDamageFactorTank[num12] = self.table5_12.FindDamageFactor(self._data.WallLossFraction[num12], (float)(self._data.NumberOfInspections), self._data.HighestInspectionEffectiveness)
                
            else:
            
                self._data.BaseDamageFactorNoTank = []
                numArray2 = []

                if (((self._data.Beta0AP == None) or (self._data.Beta1AP == None)) or (self._data.Beta2AP == None)):
                    numArray2[0] = self.defaultDF
                    numArray2[1] = self.defaultDF
                    numArray2[2] = self.defaultDF
                else:
                    #2.22
                    numArray2[0] = CalcEquation2_22.Equation2_22(self._data.PosteriorProbabilities[0],self._data.Beta0AP[0],self._data.PosteriorProbabilities[1],self._data.Beta0AP[1],self._data.PosteriorProbabilities[2],self._data.Beta0AP[2])
                    numArray2[1] = CalcEquation2_22.Equation2_22(self._data.PosteriorProbabilities[0],self._data.Beta0AP[0],self._data.PosteriorProbabilities[1],self._data.Beta0AP[1],self._data.PosteriorProbabilities[2],self._data.Beta0AP[2])
                    numArray2[2] = CalcEquation2_22.Equation2_22(self._data.PosteriorProbabilities[0],self._data.Beta0AP[0],self._data.PosteriorProbabilities[1],self._data.Beta0AP[1],self._data.PosteriorProbabilities[2],self._data.Beta0AP[2])
                if (self._data.EquipmentIsTank):
                    self._data.BaseDamageFactorTank = numArray2
                else:
                    self._data.BaseDamageFactorNoTank = numArray2
            self._data.FOM = self.table5_13.GetOnlineMonitoringAdjustmentFactor(self._data.OnlineMonitoring, True)
            if not(self._data.EquipmentIsTank):
                if ((((self._data.ComponentType == ComponentType.PIPE1) or (self._data.ComponentType == ComponentType.PIPE10)) or ((self._data.ComponentType == ComponentType.PIPE12) or (self._data.ComponentType == ComponentType.PIPE16))) or (((self._data.ComponentType == ComponentType.PIPE2) or (self._data.ComponentType == ComponentType.PIPE4)) or (((self._data.ComponentType == ComponentType.PIPE6) or (self._data.ComponentType == ComponentType.PIPE8)) or (self._data.ComponentType == ComponentType.PIPEGT16)))):
                    if self._data.ContainsInjectionPoint:
                        if (self._data.InspectionEffectiveAtPoint):
                            self._data.FIP = 1.0
                        else:
                            self._data.FIP = 3.0
                    else:
                        self._data.FIP = 1.0
                    if (not(self._data.InspectionEffectiveAtDeadleg) and self._data.ContainsDeadlegs):
                        self._data.FDL = 3.0
                    else:
                        self._data.FDL = 1.0
                else:
                    self._data.FIP = 1.0
                    self._data.FDL = 1.0
                for num14 in range(3):
                    self._data.DamageFactor[num14] = math.max((float) (((self._data.BaseDamageFactorNoTank[num14] * self._data.FIP) * self._data.FDL) / self._data.FOM), (float) (0.1))
            else:
                self._data.FWD = 10.0
                if self._data.ComponentIsWelded:
                    self._data.FWD = 1.0
                self._data.FAM = 5.0
                if self._data.MaintainAccordance:
                    self._data.FAM = 1.0
                
                if(self._data.AdjustmentSettlement == TankSettlementCondition.RecordedSettlementExceedsAPI653Criteria):
                    self._data.FSM = 2.0
                elif(self._data.AdjustmentSettlement == TankSettlementCondition.RecordedSettlementMeetsAPI653Criteria):
                    self._data.FSM = 1.0
                elif(self._data.AdjustmentSettlement == TankSettlementCondition.SettlementNeverEvaluated):
                    self._data.FSM = 1.5
                elif(self._data.AdjustmentSettlement == TankSettlementCondition.ConcreteFoundationNoSettlement):
                    self._data.FSM = 1.0
                
                for num13 in range(3):
                    self._data.DamageFactor[num13] = math.max((float) ((((self._data.BaseDamageFactorTank[num13] * self._data.FWD) * self._data.FAM) * self._data.FSM) / self._data.FOM), (float) (0.1))