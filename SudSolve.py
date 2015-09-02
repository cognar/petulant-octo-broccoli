#!../flask/bin/python
# Solves Sudokus by building a list of possible values for every blank (0) space
from math import sqrt


def sudoku(puzzlestr):
    n = int(len(puzzlestr)**0.5)
    _ = [i for i in puzzlestr[::-1]]
    puzzle = [[_.pop() for i in range(n)] for j in range(n)]
    # Builds Dictionary with board position and value
    dic = {str(i+1) + '-' + str(j+1): int(puzzle[i][j]) for i in range(0, n) for j in range(0, n)}
    # Builds list of each possible value for all empty (0) spaces, only considers row and column possibilities
    while 0 in dic.values():        # while puzzle contains unsolved positions
        for entry in dic:
            if dic[entry] == 0:
                temp1 = []
                temp2 = []
                for entry1 in dic:
                    if entry1[0] == entry[0]: temp1.append(dic[entry1])
                    if entry1[-1] == entry[-1]: temp1.append(dic[entry1])
                for i in range(1, n+1):
                    if i not in temp1: temp2.append(i)
                dic[entry] = temp2
        # populates dictionary with invalid spaces in each square
        sqrdic = {str(i)+str(j): [] for i in range(1, int(sqrt(n))+1) for j in range(1, int(sqrt(n))+1)}
        for entry in dic:
            if len(str(dic[entry])) == 1:
                for index in range(1, int(n/sqrt(n)+1)):
                    if (index-1)*sqrt(n) < int(entry[0]) <= index*sqrt(n):
                        for index2 in range(1, int(sqrt(n))+1):
                            if (index2-1)*sqrt(n) < int(entry[-1]) <= index2*sqrt(n):
                                sqrdic[str(index) + str(index2)].append(dic[entry])
        # Removes invalid choices based on values in the square
        for entry in dic:
            if len(str(dic[entry])) > 1:  # only looking at spaces with multiple possible values
                for index in range(1, int(n/sqrt(n)+1)):
                    if (index-1)*sqrt(n) < int(entry[0]) <= index*sqrt(n):
                        for index2 in range(1, int(sqrt(n))+1):
                            if (index2-1)*sqrt(n) < int(entry[-1]) <= index2*sqrt(n):
                                for i in sqrdic[str(index)+str(index2)]:
                                    if i in dic[entry]: dic[entry].remove(i)
        # Looks for any space whose possibilities have been reduced to one and replaces the list with that value
        # All unsolved spaces are then set back to 0
        for entry in dic:
            if type(dic[entry]) is list and len(dic[entry]) == 1:
                dic[entry] = int(dic[entry][0])
            elif type(dic[entry]) is list and len(dic[entry]) > 1: dic[entry] = 0
    solution = [[dic[str(j)+"-"+str(i)] for i in range(1,n+1)] for j in range(1,n+1)]
    for index, row in enumerate(solution):
        solution[index] = ''.join([str(i) for i in row])
    return ''.join(solution)
