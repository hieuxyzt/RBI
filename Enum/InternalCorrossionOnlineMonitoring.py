import enum
class InternalCorrossionOnlineMonitoring(enum.Enum):
        #[Description("Amine high velocity corrosion - corrosion coupons")]
        AmineHighVelocityCorrosion_corrosionCoupons = 0,
        #[Description("Amine high velocity corrosion - Electrical resistance probes")]
        AmineHighVelocityCorrosion_ElectricalResistanceProbes = 1,
        #[Description("Amine high velocity corrosion - Key process variable")]
        AmineHighVelocityCorrosion_KeyProcessVariable = 2,
        #[Description("Amine low velocity corrosion - corrosion coupons")]
        AminelowVelocityCorrosion_corrosionCoupons = 3,
        #[Description("Amine low velocity corrosion - Electrical resistance probes")]
        AminelowVelocityCorrosion_ElectricalResistanceProbes = 4,
        #[Description("Amine low velocity corrosion - Key process variable")]
        AminelowVelocityCorrosion_KeyProcessVariable = 5,
        #[Description("HCI corrosion - corrosion coupons")]
        HCIcorrosion_corrosionCoupons = 6,
        #[Description("HCI corrosion - Electrical resistance probes")]
        HCIcorrosion_ElectricalResistanceProbes = 7,
        #[Description("HCI corrosion - Key process variable")]
        HCIcorrosion_KeyProcessVariable = 8,
        #[Description("HCI corrosion - Key process variable & Electrical resistance probes")]
        HCIcorrosion_KeyProcessVariable_and_ElectricalResistanceProbes = 9,
        #[Description("HF corrosion - corrosion coupons")]
        HFcorrosion_corrosionCoupons = 10,
        #[Description("HF corrosion - Electrical resistance probes")]
        HFcorrosion_ElectricalResistanceProbes = 11,
        #[Description("HF corrosion - Key process variable")]
        HFcorrosion_KeyProcessVariable = 12,
        #[Description("High temperature H2S/H2 corrosion - Corrosion coupons")]
        HightemperatureH2S_H2corrosion_CorrosionCoupons = 13,
        #[Description("High temperature H2S/H2 corrosion - Electrical resistance probes")]
        HightemperatureH2S_H2corrosion_ElectricalResistanceProbes = 14,
        #[Description("High temperature H2S/H2 corrosion - Key process parameters")]
        HightemperatureH2S_H2corrosion_KeyProcessparameters = 15,
        #[Description("High temperature sulfidic/Napthenic acid corrosion - Corrosion coupons")]
        Hightemperaturesulfidic_NapthenicAcidCorrosion_CorrosionCoupons = 0x10,
        #[Description("High temperature sulfidic/Napthenic acid corrosion - Electrical resistance probes")]
        Hightemperaturesulfidic_NapthenicAcidCorrosion_ElectricalResistanceProbes = 0x11,
        #[Description("High temperature sulfidic/Napthenic acid corrosion - Key process variable")]
        Hightemperaturesulfidic_NapthenicAcidCorrosion_KeyProcessVariable = 0x12,
        #[Description("No online monitoring")]
        NoOnlineMonitoring = 0x13,
        #[Description("Other corrosion - corrosion coupons")]
        Othercorrosion_corrosionCoupons = 20,
        #[Description("Other corrosion - Electrical resistance probes")]
        Othercorrosion_ElectricalResistanceProbes = 0x15,
        #[Description("Other corrosion - Hydrogen Probes")]
        Othercorrosion_HydrogenProbes = 0x17,
        #[Description("Other corrosion - Key process variable")]
        Othercorrosion_KeyProcessVariable = 0x16,
        #[Description("Other corrosion - Key process variable and hydrogen probes")]
        Othercorrosion_KeyProcessVariablesHydrogenProbes = 0x18,
        #[Description("Sour water high velocity corrosion - corrosion coupons")]
        SourwaterHighVelocityCorrosion_corrosionCoupons = 0x19,
        #[Description("Sour water high velocity corrosion - Electrical resistance probes")]
        SourwaterHighVelocityCorrosion_ElectricalResistanceProbes = 0x1a,
        #[Description("Sour water high velocity corrosion - Key process variable")]
        SourwaterHighVelocityCorrosion_KeyProcessVariable = 0x1b,
        #[Description("Sour water low velocity corrosion - corrosion coupons")]
        SourwaterlowVelocityCorrosion_corrosionCoupons = 0x1c,
        #[Description("Sour water low velocity corrosion - Electrical resistance probes")]
        SourwaterlowVelocityCorrosion_ElectricalResistanceProbes = 0x1d,
        #[Description("Sour water low velocity corrosion - Key process variable")]
        SourwaterlowVelocityCorrosion_KeyProcessVariable = 30,
        #[Description("Sulfuric acid (H2S/H2) corrosion high velocity - Corrosion coupons")]
        Sulfuricacid_H2S_H2_corrosionHighVelocity_CorrosionCoupons = 0x1f,
        #[Description("Sulfuric acid (H2S/H2) corrosion high velocity - Electrical resistance probes")]
        Sulfuricacid_H2S_H2_corrosionHighVelocity_ElectricalResistanceProbes = 0x20,
        #[Description("Sulfuric acid (H2S/H2) corrosion high velocity - Key process parameters")]
        Sulfuricacid_H2S_H2_corrosionHighVelocity_KeyProcessparameters = 0x21,
        #[Description("Sulfuric acid (H2S/H2) corrosion high velocity - Key process parameters & electrical resistance probes")]
        Sulfuricacid_H2S_H2_corrosionHighVelocity_KeyProcessparameters_and_electricalResistanceProbes = 0x22,
        #[Description("Sulfuric acid (H2S/H2) corrosion low velocity - Corrosion coupons")]
        Sulfuricacid_H2S_H2_corrosionlowVelocity_CorrosionCoupons = 0x23,
        #[Description("Sulfuric acid (H2S/H2) corrosion low velocity - Electrical resistance probes")]
        Sulfuricacid_H2S_H2_corrosionlowVelocity_ElectricalResistanceProbes = 0x24,
        #[Description("Sulfuric acid (H2S/H2) corrosion low velocity - Key process parameters")]
        Sulfuricacid_H2S_H2_corrosionlowVelocity_KeyProcessparameters = 0x25
