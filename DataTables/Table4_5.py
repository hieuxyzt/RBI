import Table4_5Data
class Table4_5:
    data = []
    def __init__(self):
        numArray = [ 0.5, 0.3, 0.2 ]
        numArray2 = [ 0.7, 0.2, 0.1]
        numArray3 = [0.8, 0.15, 0.05] 
        item = Table4_5Data(
            LowConfidence = numArray,
            MediumConfidence = numArray2,
            HighConfidence = numArray3
        )
        self.data.append(item)
       

    def Find(self, level):
        str = level.lower()
        if str != "low":
            if str == "medium":
                return self.data[0].MediumConfidence
            if str == "high":
                return self.data[0].HighConfidence
            return 0.0
        return self.data[0].LowConfidence
      
