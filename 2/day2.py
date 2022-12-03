#!/usr/bin/python

def pointsum():
    with open('input.txt') as inputfile:
        points = 0
        for line in inputfile:
            points += int(line[-2])
            # switch case would be great here
            if line[0] == line[-2]:
                points += 3
            else:
                won = (
                    line[:-1] == '3 1' or
                    line[:-1] == '2 3' or
                    line[:-1] == '1 2'
                )
                if won:
                    points += 6
                else:
                    continue
        print(f'First part: {points}')

    with open('input.txt') as inputfile:
        points = 0
        for line in inputfile:
            outcome = (int(line[-2]) - 1) * 3
            points += outcome
            if outcome == 3:
                points += int(line[0])
            # chose 2
            elif (outcome == 6 and int(line[0]) == 1) or (outcome == 0 and int(line[0]) == 3):
                points += 2
            # chose 3
            elif (outcome == 6 and int(line[0]) == 2) or (outcome == 0 and int(line[0]) == 1):
                points += 3
            # chose 1
            elif (outcome == 6 and int(line[0]) == 3) or (outcome == 0 and int(line[0]) == 2):
                points += 1
        print(f'Second part: {points}')


if __name__ == '__main__':
    pointsum()
