list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
list2=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]

def updateList(list, noun=12, verb=2):
    list[1]= noun
    list[2] = verb
    index = 0
    while list[index] != 99:
        value = list[index]
        if value == 1:
            list[list[index+3]] = list[list[index+1]] + list[list[index+2]]
        elif value == 2:
            list[list[index+3]] = list[list[index+1]] * list[list[index+2]]
        index+=4

def findInputs(value):
    for noun in range(100):
        for verb in range(100):
            listcopy = list2.copy()
            updateList(listcopy, noun, verb)
            if listcopy[0] == value:
                return [noun, verb]



updateList(list)
solution1 = list[0]
solution2 = findInputs(19690720)
print(solution1)
print(100*solution2[0] + solution2[1])
