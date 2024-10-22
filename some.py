class TestTask:
    List = {}
    
    def __init__(self):
        pass

    def SumLogic(self,StringNumber):
        sum = 0
        for digit in str(StringNumber):  
            sum += int(digit)       
        return sum

    def AddLogic(self):
        while(True):
            try:
                num = int(input("Num: "))
                if num == 0:
                    break
                self.List[str(num)] = self.SumLogic(num)
            except ValueError: 
                print("num is not integer")
                input("Press Enter to exit")
                exit(101)

TestObject=TestTask()
TestObject.AddLogic()
print("Answer: " + max(TestObject.List,key=TestObject.List.get))
input("Press Enter to exit")
