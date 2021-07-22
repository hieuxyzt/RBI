from ..Enum import InternalCorrossionOnlineMonitoring
class Table5_13:
    data = {}

    def GetOnlineMonitoringAdjustmentFactor(self, monitoring, isThinning = False):
        if self.data == None:
            
            self.Init(isThinning)
          
        return self.data[monitoring]
    

    def Init(self, IsThining):
        self.data = {}
        self.data.Add(InternalCorrossionOnlineMonitoring.AmineHighVelocityCorrosion_corrosionCoupons, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.AmineHighVelocityCorrosion_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.AmineHighVelocityCorrosion_KeyProcessVariable, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.AminelowVelocityCorrosion_corrosionCoupons, 2)
        self.data.Add(InternalCorrossionOnlineMonitoring.AminelowVelocityCorrosion_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.AminelowVelocityCorrosion_KeyProcessVariable, 20)
        self.data.Add(InternalCorrossionOnlineMonitoring.HCIcorrosion_corrosionCoupons, 2)
        self.data.Add(InternalCorrossionOnlineMonitoring.HCIcorrosion_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.HCIcorrosion_KeyProcessVariable, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.HCIcorrosion_KeyProcessVariable_and_ElectricalResistanceProbes, 20)
        self.data.Add(InternalCorrossionOnlineMonitoring.HFcorrosion_corrosionCoupons, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.HFcorrosion_ElectricalResistanceProbes, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.HFcorrosion_KeyProcessVariable, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.HightemperatureH2S_H2corrosion_CorrosionCoupons, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.HightemperatureH2S_H2corrosion_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.HightemperatureH2S_H2corrosion_KeyProcessparameters, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.Hightemperaturesulfidic_NapthenicAcidCorrosion_CorrosionCoupons, 2)
        self.data.Add(InternalCorrossionOnlineMonitoring.Hightemperaturesulfidic_NapthenicAcidCorrosion_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.Hightemperaturesulfidic_NapthenicAcidCorrosion_KeyProcessVariable, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.NoOnlineMonitoring, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_corrosionCoupons, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_ElectricalResistanceProbes, 1)
        if IsThining:
                self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_KeyProcessVariable, 1)
                self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_HydrogenProbes, 1)
                self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_KeyProcessVariablesHydrogenProbes, 1)
 
        else:
                self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_KeyProcessVariable, 2)
                self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_HydrogenProbes, 2)
                self.data.Add(InternalCorrossionOnlineMonitoring.Othercorrosion_KeyProcessVariablesHydrogenProbes, 4)

        self.data.Add(InternalCorrossionOnlineMonitoring.SourwaterHighVelocityCorrosion_corrosionCoupons, 2)
        self.data.Add(InternalCorrossionOnlineMonitoring.SourwaterHighVelocityCorrosion_ElectricalResistanceProbes, 2)
        self.data.Add(InternalCorrossionOnlineMonitoring.SourwaterHighVelocityCorrosion_KeyProcessVariable, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.SourwaterlowVelocityCorrosion_corrosionCoupons, 2)
        self.data.Add(InternalCorrossionOnlineMonitoring.SourwaterlowVelocityCorrosion_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.SourwaterlowVelocityCorrosion_KeyProcessVariable, 20)
        self.data.Add(InternalCorrossionOnlineMonitoring.Sulfuricacid_H2S_H2_corrosionHighVelocity_CorrosionCoupons, 1)
        self.data.Add(InternalCorrossionOnlineMonitoring.Sulfuricacid_H2S_H2_corrosionHighVelocity_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.Sulfuricacid_H2S_H2_corrosionHighVelocity_KeyProcessparameters, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.Sulfuricacid_H2S_H2_corrosionHighVelocity_KeyProcessparameters_and_electricalResistanceProbes, 20)
        self.data.Add(InternalCorrossionOnlineMonitoring.Sulfuricacid_H2S_H2_corrosionlowVelocity_CorrosionCoupons, 2)
        self.data.Add(InternalCorrossionOnlineMonitoring.Sulfuricacid_H2S_H2_corrosionlowVelocity_ElectricalResistanceProbes, 10)
        self.data.Add(InternalCorrossionOnlineMonitoring.Sulfuricacid_H2S_H2_corrosionlowVelocity_KeyProcessparameters, 20)
 
