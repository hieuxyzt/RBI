import Table4_6Data
class Table4_6:
        data = []

        def __init__(self):
           
            numArray = [0.9, 0.09, 0.01 ]
            numArray2 = [ 0.7, 0.2, 0.1 ]
            numArray3 = [0.5, 0.3, 0.2 ]
            numArray4 =  [0.4, 0.33, 0.27] 
            numArray5 =  [0.33, 0.33, 0.33 ]
            item = Table4_6Data(
                A = numArray,
                B = numArray2,
                C = numArray3,
                D = numArray4,
                E = numArray5
            )
            self.data.append(item)

        def GetConditionalProbability(self,input):
        
            if (input > self.data[0].A.Length) or (input < 0):
            
                return None
            
            return [ self.data[0].A[input], self.data[0].B[input], self.data[0].C[input], self.data[0].D[input], self.data[0].E[input] ]
