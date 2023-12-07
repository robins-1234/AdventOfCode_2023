import re

def readInput():
    file = open('Day_02\input.txt', 'r')
    result =file.readlines()
    file.close
    return result


def main(input):
    limits = [12, 13, 14]
    colors =["red", "green", "blue"]
    finalCount = 0

    
    for line in input:
        validGame = True
        ID = line[line.find("Game ")+5:line.find(":")]
        
        for i in range(0,3):
            regex = "\d*."+colors[i]
            result = re.findall(regex,line)
            for count in result:
                count = count[0:count.find(" ")]
                if int(count) > limits[i]:
                    validGame = False  


        if validGame:
            finalCount += int(ID)
    print(finalCount)
        

main(readInput())