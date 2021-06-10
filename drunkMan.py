import random

times = [[0 for i in range(11)] for j in range(11)]
move = ['right', 'left', 'up', 'down', 'right_up_diagonal', 'right_down_diagonal', 'left_up_diagonal',
        'left_down_diagonal']
for i in times:
    for j in i:
        print(j, end=" ")
    print()


def drunkWalk (row, col):

    times[row][col] += 1

    print("Movement : \n")
    for i in times:
        for j in i:
            print(j, end=" ")
        print()
    while( times[0][0] == times[0][10] == times[10][0] == times[10][10] ):
        position1 = row
        position2 = col
        if position2 == 0:
            step = random.choice([ele for ele in move if ele != "right" and ele != "right_up_diagonal" and
                                  ele != "right_down_diagonal"])
        elif position2 == 10:
            step = random.choice([ele for ele in move if ele != "left" and ele != "left_up_diagonal" and
                                  ele != "left_down_diagonal"])
        elif position1 == 0:
            step = random.choice([ele for ele in move if ele != "top" and ele != "right_up_diagonal" and
                                  ele != "left_up_diagonal"])
        elif position1 == 10:
            step = random.choice([ele for ele in move if ele != "down" and ele != "right_down_diagonal" and
                                  ele != "left_down_diagonal"])
        else:
            step = random.choice(move)
        print("\nMoving to:", step)
        if step == "right":
            position1 = row
            position2 = col-1
            return drunkWalk(position1,position2)
        elif step == "left":
            position1 = row
            position2 = col + 1
            return drunkWalk(position1, position2)
        elif step == "up":
            position1 = row - 1
            position2 = col
            return drunkWalk(position1, position2)
        elif step == "down":
            position1 = row + 1
            position2 = col
            return drunkWalk(position1, position2)
        elif step == "right_up_diagonal":
            position1 = row - 1
            position2 = col - 1
            return drunkWalk(position1, position2)
        elif step == "right_down_diagonal":
            position1 = row + 1
            position2 = col - 1
            return drunkWalk(position1, position2)
        elif step == "left_up_diagonal":
            position1 = row - 1
            position2 = col + 1
            return drunkWalk(position1, position2)
        else:
            position1 = row + 1
            position2 = col + 1
            return drunkWalk(position1, position2)


sim = drunkWalk(5, 5)
print (sim)
print("End of journey!!")