import datetime
class CalcHelpers:
    #commission/inspection period //da test
    def Ap(AssessmentPeriod):
        return [0,AssessmentPeriod,AssessmentPeriod*2]
    def ConvertToDay(Date):
        return Date.seconds/3600.0/24.0
    def ConvertToYear(Date):
        return Date.seconds/3600.0/24.0/365.25
    def InServiceTime(AssessmentDate, ParameterDate, AP ):
        numArray=[]
        for i in range(3):
            timeSpan = AssessmentDate - ParameterDate
            numArray.append(max(0.0,
            CalcHelpers.ConvertToYear(timeSpan)+
            (float)(AP[i])/12.0)
            )
        return numArray

    def YearsFromCommisionDate(RiskwiseAssessmentDate, StartOrCommissioningDate, AssessmentPeriod):
        numArray = []
        timeSpan = RiskwiseAssessmentDate - StartOrCommissioningDate
        element = CalcHelpers.ConvertToYear(timeSpan) + 0.0/12.0
        if(element<0.0):
            element = 0
        else:
            numArray.append(element)
        element = CalcHelpers.ConvertToYear(timeSpan) + AssessmentPeriod/12.0
        if(element<0.0):
            element = 0
        else:
            numArray.append(element)
        element = CalcHelpers.ConvertToYear(timeSpan) + 2*AssessmentPeriod/12.0
        if(element<0.0):
            element = 0
        else:
            numArray.append(element)
        return numArray 
test = CalcHelpers.YearsFromCommisionDate(datetime.datetime.now(),datetime.datetime(2021,7,19),36)



