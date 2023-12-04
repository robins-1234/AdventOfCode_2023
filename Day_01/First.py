def readInput():
    file = open('Day_01\Input.txt', 'r')
    result =file.readlines()
    file.close
    return result

def main(input):
    finalresult = 0
    for line in input:
        signList = [signList for signList in line]
        result = ""
        for sign in signList:
            if sign.isdigit():
                result += sign            
        if len(result) < 2:
            result += result
        if len(result) > 2:
            result = result[0]+result[len(result)-1]
        finalresult += int(result)
    print(finalresult)

input = readInput()
main(input)
    