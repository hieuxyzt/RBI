class TankSettlementCondition:
    #"Concrete foundation, no settlement"
    ConcreteFoundationNoSettlement = 4,
    #"Not Applicable"
    NotApplicable = 0,
    #"Recorded settlement exceeds API STD 653 criteria"
    RecordedSettlementExceedsAPI653Criteria = 1,
    #"Recorded settlement meets API STD 653 criteria"
    RecordedSettlementMeetsAPI653Criteria = 2,
    #"Settlement never evaluated"
    SettlementNeverEvaluated = 3