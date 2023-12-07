def readInput():
    file = open('Day_01\Input.txt', 'r')
    result =file.readlines()
    file.close
    return result

def getValueOf(text:str):
    if text == "one":
        return 1
    elif text == "two":
        return 2
    elif text == "three":
        return 3
    elif text == "four":
        return 4
    elif text == "five":
        return 5
    elif text == "six":
        return 6
    elif text == "seven":
        return 7
    elif text == "eight":
        return 8
    elif text == "nine":
        return 9


def main(input):
    digitlist = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    result = 0
    for line in input:
        numberArray = []

        while line != "":
            index = 0
            c = line[index]
            
            if c.isdigit():
                numberArray.append(int(c))
                line = line[1:len(line)]
                                
            else:
                for digit in digitlist:
                    for digitChar in digit:
                        if c == digitChar:
                            ##still completing digits
                            index += 1
                            if index < len(line):
                                c = line[index]
                        else:
                            ##currentDigit is false
                            if digit == "nine":
                                line = line[1:len(line)]
                            else:
                                index = 0
                                if line != "":
                                    c = line[index]
                            break
                        if index == len(digit):
                            ##digit is complete
                            line = line[1:len(line)]
                            numberArray.append(getValueOf(digit))
                            break

        firstValue = str(numberArray[0])
        secondValue = str(numberArray[len(numberArray)-1])
        currentIteration = int(firstValue+secondValue)
        result += currentIteration
    print(result)
                

input = readInput()
main(input)
    