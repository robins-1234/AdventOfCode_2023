def readInput():
    file = open('Day_03\input.txt', 'r')
    result =file.readlines()
    file.close
    return result



class Number:
    def __init__(self, value:int, start_x:int, start_y:int, end_x:int, end_y:int):
        self.value = value 
        self.start_x = start_x
        self.start_y = start_y 
        self.end_x = end_x
        self.end_y = end_y

class Symbol:    
    def __init__(self, sign:str, x:int, y:int):
        self.sign = sign 
        self.x = x
        self.y = y
        self.numberA = None
        self.numberB = None
        self.complete = False
        self.ratio = None

    def addNumber(self, number:Number):
        if self.numberA == None:
            self.numberA = number
        elif self.numberB == None:
            self.numberB = number
            self.complete = True
        else:
            self.complete = False
    
    def isComplete(self) -> bool:
        return self.complete
    
    def getRatio(self) -> int:
        return self.numberA.value * self.numberB.value
    
def main(input):
    ##gather symbols
    symbollist = []
    y = 0    

    for line in input:
        y+= 1
        x = 0
        for sign in line:
            x+= 1
            if sign == '*':
                ##symbol found
                symbollist.append(Symbol(sign,x, y))

    ##check numbers
    y = 0
    numberlist = []
    for line in input:
        y+= 1
        x = 0
        currentNumber= []
        countingDigit = False
        for sign in line:
            x+= 1
            if (sign.isdigit()) & (not countingDigit):
                ##numberstart
                countingDigit = True
                start = x
            if (sign.isdigit()) & countingDigit:
                currentNumber.append(sign)
                
            if (not sign.isdigit()) & countingDigit:
                ##numberend
                countingDigit = False
                end = x-1
                result = ""
                for number in currentNumber:
                    result += str(number)
                currentNumber= []
                numberlist.append(Number(int(result),start,y, end,y))

    ##compare:
    for number in numberlist:
        for symbol in symbollist:
            for i in range(-1, 2):
                if (symbol.x >= number.start_x-1) & (symbol.x <= number.end_x+1) & (symbol.y == number.start_y+i):
                    symbol.addNumber(number)

    result = 0
    for symbol in symbollist:
        if symbol.isComplete():
            result += symbol.getRatio()
    print(result)                 


main(readInput())



