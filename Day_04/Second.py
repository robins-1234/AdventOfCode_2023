import re

def readInput():
    file = open('Day_04\input.txt', 'r')
    result =file.readlines()
    file.close
    return result

def main(input):
    regex = "\d+"    
    result = 0  

    copystack=[]

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

        result += numberOfPlays  

        for i in range(0, wins):
            if len(copystack) > i:
                copystack[i] = copystack[i]+numberOfPlays
            else: 
                copystack.append(numberOfPlays)       

    print(result)

main(readInput())