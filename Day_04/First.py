import re
import math

def readInput():
    file = open('Day_04\input.txt', 'r')
    result =file.readlines()
    file.close
    return result

def main(input):
    regex = "\d+"    
    result = 0

    for line in input:
        count = 0

        winnerpart = line[line.find(':')+1:line.find('|')]
        handpart = line[line.find('|'):len(line)]
        winners = re.findall(regex,winnerpart)
        hand = re.findall(regex, handpart)

        for number in hand:
            for winner in winners:
                if number == winner:
                    count += 1
        
        if count > 0:
            result += int(math.pow(2,count-1))
    
    print(result)

main(readInput())



