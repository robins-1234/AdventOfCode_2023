import re
import math

def readInput():
    file = open('Day_04\input.txt', 'r')
    result =file.readlines()
    file.close
    return result


##calc wins: original + number in first stack entry, remove entry from stack
##for each win: add entry in stack

def main(input):
    regex = "\d+"  

    copystack=[]
    resultlist=[]

    for line in input:
        wins = 0

        winnerpart = line[line.find(':')+1:line.find('|')]
        handpart = line[line.find('|'):len(line)]
        winners = re.findall(regex,winnerpart)
        hand = re.findall(regex, handpart)

        
        for number in hand:
            for winner in winners:
                if number == winner:
                    wins += 1

        numberOfPlays = 1
        if len(copystack) > 0:
            numberOfPlays += copystack[0]
            del copystack[0]
            
        resultlist.append(numberOfPlays)

        for i in range(0, wins):
            if len(copystack) > i:
                copystack[i] = copystack[i]+numberOfPlays
            else: 
                copystack.append(numberOfPlays)

          
    result = 0
    for cardCount in resultlist:
        result += cardCount    
    print(result)

main(readInput())



