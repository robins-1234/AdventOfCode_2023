import re

def readInput():
    file = open('Day_02\input.txt', 'r')
    result =file.readlines()
    file.close
    return result


def main(input):
    colors =["red", "green", "blue"]
    finalCount = 0
    
    for line in input:
        max =[0,0,0]
        
        for i in range(0,3):
            regex = "\d*."+colors[i]
            result = re.findall(regex,line)
            for count in result:
                count = count[0:count.find(" ")]
                if int(count) > max[i]:
                    max[i]=int(count) 

        power = max[0]*max[1]*max[2]

        finalCount += power
    print(finalCount)
           

main(readInput())